# Melissa: Your Virtual AI Assistant

Melissa is a virtual AI assistant for macOS, Windows, and Linux systems. It uses Ollama to access local LLM models and Vosk for speech-to-text conversion.

The code is part of the book - Building a Virtual Assistant for Raspberry Pi (Edition 2), written by [Harshil Agrawal](https://harshil.dev) and [Tanay Pant](https://github.com/tanay1337).

## Running

Run Melissa with `python src/main.py`. By default, Melissa uses the microphone and audio output. Use `--mode type` for console input and output:

```sh
python src/main.py --mode type
python src/main.py --mode speak
```

In either mode, an empty input ends the conversation.

## Support

If you run into any problems, please open up a new issue.

## License

[MIT License](./LICENSE)
