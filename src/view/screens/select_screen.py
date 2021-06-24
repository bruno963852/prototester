from view.ui import OLED, CHARACTER_SIZE  # pylint: disable=import-error
# from view.icon_draw import draw_icon # pylint: disable=import-error
# from view.icons import prototester # pylint: disable=import-error

TITLE = "SELECT"
TEXTVIEW_X = 10
TEXTVIEW_Y = 12
TEXTVIEW_WIDTH = 118
TEXTVIEW_HEIGHT = 52
PADDING = 1
SPACING = 2

class SelectScreen:
    def __init__(self, pages_quant: int):
        self.pages = pages_quant

    def show(self, options: list, selected_in_page: int, page_index: int):
        oled = OLED.instance()
        oled.clear()
        oled.draw_window(
            TITLE, right_text='{}/{}'.format(page_index + 1, self.pages))
        oled.draw_list_view(TEXTVIEW_X, TEXTVIEW_Y, TEXTVIEW_WIDTH, TEXTVIEW_HEIGHT,
                            options, padding=PADDING, spacing=SPACING)
        arrow_position = TEXTVIEW_Y + PADDING + (selected_in_page * (SPACING + CHARACTER_SIZE))
        oled.draw_text('>', 2, arrow_position)
        oled.show()
