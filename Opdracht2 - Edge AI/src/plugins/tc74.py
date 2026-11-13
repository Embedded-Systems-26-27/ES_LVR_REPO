from smbus2 import SMBus

TC74_ADDR = 0x48  # TC74A0; controleer met `i2cdetect -y 1`


def read_temperature() -> str:
    with SMBus(1) as bus:
        t = bus.read_byte_data(TC74_ADDR, 0x00)
    t = t - 256 if t > 127 else t
    return f"De temperatuur is {t} graden Celsius."
