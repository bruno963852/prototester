import math
from machine import Pin, I2C
from micropython import const
from ssd1306 import SSD1306_I2C # pylint: disable=import-error
from view.icon_draw import draw_icon # pylint: disable=import-error

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
        self._i2c = I2C(0, scl=Pin(22), sda=Pin(21))
        self._oled = SSD1306_I2C(128, 64, self._i2c)

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

    def draw_window(self, title: str, left_text: str = None, right_text: str = ""):
        self._oled.rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_WHITE)
        self._oled.fill_rect(0, 0, SCREEN_WIDTH, CHARACTER_SIZE + 4, COLOR_WHITE)
        self.draw_text_in_center(title, 2)
        title_width_pixels = len(title) * CHARACTER_SIZE
        max_text_size = math.floor(SCREEN_WIDTH - title_width_pixels) - 1
        if left_text:
            text_width_pixels = len(left_text) * CHARACTER_SIZE
            if text_width_pixels > max_text_size:
                raise ValueError("Left Text Too Big...")
            self._oled.text(left_text, 0, 2, COLOR_BLACK)
        if right_text:
            text_width_pixels = len(right_text) * CHARACTER_SIZE
            if text_width_pixels > max_text_size:
                raise ValueError("Right Text Too Big...")
            self._oled.text(right_text, SCREEN_WIDTH - text_width_pixels, 2, COLOR_BLACK)

    def draw_text_in_center(self, text: str, y_position):
        text_width_pixels = len(text) * CHARACTER_SIZE
        left_padding = int((SCREEN_WIDTH - text_width_pixels) / 2)
        self.draw_text_with_background(text, left_padding, y_position)

    def draw_text_with_background(self, text: str, position_x: int, position_y: int, text_color: int = COLOR_WHITE, bg_color: int = COLOR_BLACK, bg_offset: int = 1):
        text_width_pixels = len(text) * CHARACTER_SIZE
        self._oled.fill_rect(position_x - bg_offset, position_y - bg_offset, text_width_pixels + (2 * bg_offset), CHARACTER_SIZE + (2 * bg_offset), bg_color)
        self._oled.text(text, position_x, position_y, text_color)

    def draw_icon(self, icon, position_x, position_y):
        draw_icon(self._oled, icon, position_x, position_y)

    def draw_icon_center(self, icon, position_y):
        icon_width, _ = self.get_icon_size(icon)
        left_padding = int((SCREEN_WIDTH - icon_width) / 2)
        self.draw_icon(icon, left_padding, position_y)

    @staticmethod
    def get_icon_size(icon):
        return int.from_bytes(icon[:2], 'big'), int.from_bytes(icon[2:4], 'big')
