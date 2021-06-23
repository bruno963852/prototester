from statemachine.start import Start # pylint: disable=import-error,no-name-in-module

class StateMachine:
    def __init__(self):
        self.stop = False

    def run(self):
        current = Start()
        while True:
            current.run()
            current = current.next()
