import inspect
import re
from ollama import chat
from plugins.getDateAndTime import get_current_date, get_current_time
from plugins.getHackerNews import get_hackernews_info
from plugins.getWeather import get_weather
from plugins.notesManager import save_note, get_note, list_notes, update_note, delete_note, search_notes
from plugins.gpioOutput import set_led
from plugins.gpioInput import read_button
from plugins.tc74 import read_temperature

available_functions = {f.__name__: f for f in [
    get_current_date, get_current_time, get_hackernews_info, get_weather,
    save_note, get_note, list_notes, update_note, delete_note, search_notes,
    set_led, read_button, read_temperature]}


def tool(name, description, props=None, required=()):
    """Bouw een tool-schema. props: {naam: beschrijving} (type string)."""
    properties = {k: {"type": "string", "description": v} for k, v in (props or {}).items()}
    return {"type": "function", "function": {
        "name": name, "description": description,
        "parameters": {"type": "object", "properties": properties, "required": list(required)}}}


tools = [
    tool("get_current_date", "Get today's date"),
    tool("get_current_time", "Always get the current time of the day"),
    tool("get_hackernews_info", "Get top stories from HackerNews",
         {"query": "The user's query about HackerNews stories"}),
    tool("get_weather", "Always get weather information for a specific city",
         {"city": "The name of the city to get weather information for"}, ["city"]),
    tool("save_note", "Save a note with a title and content",
         {"title": "The title of the note", "content": "The content of the note"}, ["title", "content"]),
    tool("get_note", "Retrieve a note by its title", {"title": "The title of the note to retrieve"}, ["title"]),
    tool("search_notes", "Search for notes containing a specific term",
         {"query": "The search term to find in notes"}, ["query"]),
    tool("list_notes", "List all available notes"),
    tool("update_note", "Update an existing note with new content",
         {"title": "The title of the note to update", "content": "The new content for the note"},
         ["title", "content"]),
    tool("delete_note", "Delete a note by its title", {"title": "The title of the note to delete"}, ["title"]),
    tool("set_led", "Turn the LED on or off", {"state": "Either 'on' or 'off'"}, ["state"]),
    tool("read_button", "Read whether the push button is pressed"),
    tool("read_temperature", "Read the current temperature in Celsius from the TC74 sensor"),
]


def clean(message):
    if message.content:
        message.content = re.sub(r'<think>.*?</think>', '', message.content, flags=re.DOTALL).strip()
    return message


def logic(messages):
    """Process messages and handle tool calls. Returns the LLM's response message."""
    response = chat(model='qwen-pi', messages=messages, tools=tools)
    clean(response.message)

    if not response.message.tool_calls:
        print('No tool calls detected')
        return response.message

    tool_outputs = []
    for call in response.message.tool_calls:
        if function_to_call := available_functions.get(call.function.name):
            # Drop arguments the model invented that the function doesn't accept
            accepted = inspect.signature(function_to_call).parameters
            arguments = {k: v for k, v in (call.function.arguments or {}).items() if k in accepted}
            try:
                output = function_to_call(**arguments)
            except Exception as e:
                output = f"Fout bij {call.function.name}: {e}"
            if output:
                tool_outputs.append({'role': 'tool', 'content': str(output), 'name': call.function.name})

    if not tool_outputs:
        return response.message

    messages.append({'role': 'assistant', 'content': response.message.content or '',
                     'tool_calls': response.message.tool_calls})
    messages.extend(tool_outputs)
    return clean(chat('qwen-pi', messages=messages, tools=tools).message)
