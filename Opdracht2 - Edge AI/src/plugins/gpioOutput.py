from gpiozero import LED

LED_PIN = 17
_led = LED(LED_PIN)  # module-niveau, zodat de status behouden blijft


def set_led(state: str) -> str:
    """Zet de LED 'on' of 'off'."""
    if state.lower() in ("on", "aan", "true", "1"):
        _led.on()
        return "De LED is aangezet."
    _led.off()
    return "De LED is uitgezet."
