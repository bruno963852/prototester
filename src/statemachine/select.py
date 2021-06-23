import uos
import math
from micropython import const
from statemachine.state import State # pylint: disable=import-error,no-name-in-module
from view.screens.select_screen import SelectScreen # pylint: disable=import-error,no-name-in-module
from buttoncontroller import ButtonController # pylint: disable=import-error,no-name-in-module

MAX_ITEMS = const(5)

class Select(State):
    def __init__(self):
        self.options = uos.listdir('protocols')
        self.pages = math.ceil(len(self.options) / MAX_ITEMS)
        self.selected = 0
        self.screen = SelectScreen(self.pages)

    @property
    def page_index(self) -> int:
        return math.floor(self.selected / MAX_ITEMS)

    @property
    def page(self) -> list:
        start = self.page_index * MAX_ITEMS
        return self.options[start: start + MAX_ITEMS]

    @property
    def selected_in_page(self):
        return self.selected % MAX_ITEMS

    def show(self):
        self.screen.show(self.page, self.selected_in_page, self.page_index)

    def run(self):
        self.show()
        btn_controller = ButtonController.instance()
        btn_controller.set_handler(ButtonController.DOWN, self.increment_selecion)
        btn_controller.set_handler(ButtonController.UP, self.decrement_selection)
        while True:
            pass

    def next(self):
        ButtonController.instance().clear_handlers()
        return Select()

    def increment_selecion(self, _):
        if self.selected >= len(self.options) - 1:
            self.selected = 0
        else:
            self.selected += 1
        self.show()

    def decrement_selection(self, _):
        if self.selected == 0:
            self.selected = len(self.options) - 1
        else:
            self.selected -= 1
        self.show()
