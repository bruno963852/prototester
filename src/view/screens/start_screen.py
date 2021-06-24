from view.ui import OLED, SCREEN_HEIGHT, CHARACTER_SIZE # pylint: disable=import-error
from view.icons import prototester # pylint: disable=import-error

TITLE = "PROTOTESTER"
SUBTITLE = "Press Button"
SPACING = 2

class StartScreen:
    @staticmethod
    def show():
        oled = OLED.instance()
        oled.clear()
        oled.draw_window(TITLE)
        oled.draw_icon_center(prototester, 15)
        oled.draw_text_in_center(SUBTITLE, SCREEN_HEIGHT - CHARACTER_SIZE - 2)
        oled.show()
