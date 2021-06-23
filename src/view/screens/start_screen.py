from view.ui import OLED # pylint: disable=import-error
from view.icon_draw import draw_icon # pylint: disable=import-error
from view.icons import prototester # pylint: disable=import-error

TITLE = "PROTOTESTER"
SUBTITLE = "Press Button"
SPACING = 2

class StartScreen:
    @staticmethod
    def show():
        oled = OLED.instance()
        oled.fill(0)
        oled.rect(0, 0, 128, 64, 255)
        oled.fill_rect(0, 0, 18, 8 + SPACING, 0xff)
        oled.fill_rect(110, 0, 18, 8 + SPACING, 0xff)
        oled.text(TITLE, int((128 - (len(TITLE) * 8)) / 2), 2)
        draw_icon(oled, prototester, int((128 - 22) / 2) + 1, 15)
        oled.text(SUBTITLE, int((128 - (len(SUBTITLE) * 8)) / 2), 54)
        oled.show()
