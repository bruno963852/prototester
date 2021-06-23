from machine import Pin

PIN_CENTER = 39
PIN_UP = 34
PIN_DOWN = 36
PIN_LEFT = 33
PIN_RIGHT = 32

class ButtonController:
    _instance = None

    CENTER = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    def __init__(self):
        self._center_pin = Pin(PIN_CENTER, Pin.IN)
        self._up_pin = Pin(PIN_UP, Pin.IN)
        self._down_pin = Pin(PIN_DOWN, Pin.IN)
        self._left_pin = Pin(PIN_LEFT, Pin.IN)
        self._right_pin = Pin(PIN_RIGHT, Pin.IN)

        self._on_center = None
        self._on_up = None
        self._on_down = None
        self._on_left = None
        self._on_right = None

        self.clear_handlers()

    @classmethod
    def instance(cls) -> ButtonController: # pylint: disable=undefined-variable
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def set_handler(self, handler_type, callback):
        if handler_type == self.CENTER:
            self._center_pin.irq(handler=callback, trigger=Pin.IRQ_FALLING)
        elif handler_type == self.UP:
            self._up_pin.irq(handler=callback, trigger=Pin.IRQ_FALLING)
        elif handler_type == self.DOWN:
            self._down_pin.irq(handler=callback, trigger=Pin.IRQ_FALLING)
        elif handler_type == self.LEFT:
            self._left_pin.irq(handler=callback, trigger=Pin.IRQ_FALLING)
        elif handler_type == self.RIGHT:
            self._right_pin.irq(handler=callback, trigger=Pin.IRQ_FALLING)

    def clear_handlers(self):
        self._center_pin.irq(handler=lambda _: None, trigger=Pin.IRQ_FALLING)
        self._up_pin.irq(handler=lambda _: None, trigger=Pin.IRQ_FALLING)
        self._down_pin.irq(handler=lambda _: None, trigger=Pin.IRQ_FALLING)
        self._left_pin.irq(handler=lambda _: None, trigger=Pin.IRQ_FALLING)
        self._right_pin.irq(handler=lambda _: None, trigger=Pin.IRQ_FALLING)
