import uos
from micropython import const
from statemachine.state import State # pylint: disable=import-error,no-name-in-module
from view.screens.select_screen import SelectScreen # pylint: disable=import-error,no-name-in-module
from buttoncontroller import ButtonController # pylint: disable=import-error,no-name-in-module

MAX_ITEMS = const(5)

class Select(State):
    def __init__(self):
        self.options = uos.listdir('protocols')
        self.window = self.options[:MAX_ITEMS]
        self.offset = 0
        self.selected = 0
        self.screen = SelectScreen()

    def run(self):
        self.screen.show(self.window, self.selected)
        btn_controller = ButtonController.instance()
        btn_controller.set_handler(ButtonController.DOWN, self.increment_selecion)
        btn_controller.set_handler(ButtonController.UP, self.decrement_selection)
        while True:
            pass

    def next(self):
        ButtonController.instance().clear_handlers()
        return Select()

    def increment_selecion(self, _):
        if self.selected >= len(self.window) - 1:
            if self.selected >= len(self.options):
                self.selected = 0
                self.offset = 0
            else:
                self.selected += 1
                self.offset += 1
                self.window = self.options[self.offset:MAX_ITEMS + self.offset]
        else:
            self.selected += 1
        self.screen.show(self.options, self.selected)

    def decrement_selection(self, _):
        if self.selected < self.offset:
            if self.selected == 0:
                self.selected = len(self.options) - 1
        else:
            self.selected -= 1
        self.screen.show(self.options, self.selected)
