from gpiozero import Button

BUTTON_PIN = 27
_button = Button(BUTTON_PIN)


def read_button() -> str:
    return "De knop is ingedrukt." if _button.is_pressed else "De knop is niet ingedrukt."
