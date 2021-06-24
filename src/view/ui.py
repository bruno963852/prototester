from machine import Pin, I2C
from micropython import const
from ssd1306 import SSD1306_I2C # pylint: disable=import-error

SCL = const(22)
SDA = const(21)

SCREEN_WIDTH = const(128)
SCREEN_HEIGHT = const(64)

CHARACTER_SIZE = const(8)

COLOR_BLACK = const(0x00)
COLOR_WHITE = const(0xff)

class OLED:
    _instance = None

    def __init__(self):
        self._i2c = I2C(0, scl=Pin(SCL), sda=Pin(SDA))
        self._oled = SSD1306_I2C(SCREEN_WIDTH, SCREEN_WIDTH, self._i2c)

    @classmethod
    def instance(cls) -> OLED: # pylint: disable=undefined-variable
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @property
    def oled(self) -> SSD1306_I2C:
        return self._oled

    def clear(self):
        self._oled.fill(COLOR_BLACK)

    def show(self):
        self._oled.show()

    def draw_window(self, title: str):
        self._oled.rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_WHITE)
        self._oled.fill_rect(0, 0, SCREEN_WIDTH, CHARACTER_SIZE + 2, COLOR_WHITE)
        # self.draw_text_in_center(title, 2)

    def draw_text_in_center(self, text: str, y_position):
        text_width_pixels = len(text) * 8
        left_padding = int((SCREEN_WIDTH - text_width_pixels) / 2)
        self._oled.text(text, left_padding, y_position)
