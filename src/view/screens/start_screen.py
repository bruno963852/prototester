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
        oled.clear()
        oled.draw_window(TITLE)
        oled.show()
