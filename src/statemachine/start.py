from statemachine.state import State # pylint: disable=import-error,no-name-in-module
from statemachine.select import Select # pylint: disable=import-error,no-name-in-module
from view.screens.start_screen import StartScreen # pylint: disable=import-error,no-name-in-module
from buttoncontroller import ButtonController # pylint: disable=import-error,no-name-in-module

class Start(State):
    def __init__(self):
        self.btn_pressed = False

    def run(self):
        ButtonController.instance().set_handler(ButtonController.CENTER, self._on_btn_pressed)
        StartScreen().show()
        while not self.btn_pressed:
            pass

    def next(self):
        ButtonController.instance().clear_handlers()
        return Select()

    def _on_btn_pressed(self, _):
        self.btn_pressed = True
