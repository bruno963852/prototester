from machine import Pin, I2C
from ssd1306 import SSD1306_I2C # pylint: disable=import-error

class OLED:
    _instance = None

    def __init__(self):
        self._i2c = I2C(0, scl=Pin(22), sda=Pin(21))
        self._oled = SSD1306_I2C(128, 64, self._i2c)

    @classmethod
    def instance(cls) -> SSD1306_I2C: # pylint: disable=undefined-variable
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance.oled

    @property
    def oled(self) -> SSD1306_I2C:
        return self._oled