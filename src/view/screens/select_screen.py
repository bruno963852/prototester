from view.ui import OLED # pylint: disable=import-error
# from view.icon_draw import draw_icon # pylint: disable=import-error
# from view.icons import prototester # pylint: disable=import-error

TITLE = "SELECT"
SPACING = 2
CHAR_HEIGHT = 8

class SelectScreen:
    def __init__(self, pages_quant: int):
        self.pages = pages_quant

    def show(self, options: list, selected_in_page: int, page_index: int):
        oled = OLED.instance().oled
        oled.fill(0)
        oled.rect(0, 0, 128, 64, 255)
        oled.text(TITLE, int((128 - (len(TITLE) * 8)) / 2), SPACING)
        oled.fill_rect(0, 0, 38, 8 + SPACING, 0xff)
        oled.fill_rect(len(TITLE) * 8 + 42, 0, 38, 8 + SPACING, 0xff)
        oled.text('{}/{}'.format(page_index + 1, self.pages), 103, SPACING, 0x00)
        for index, option in enumerate(options):
            y_position = ((index + 1) * SPACING) + ((index + 1)* CHAR_HEIGHT) + SPACING
            if index == selected_in_page:
                oled.text('>', SPACING, y_position)
            else:
                oled.fill_rect(SPACING, y_position, 8, 8, 0)
            oled.text(option.replace('.json', '')[:14], 10, y_position)
        oled.show()
