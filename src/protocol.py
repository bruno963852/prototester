import sys
import utime
import ubinascii
from select import poll, POLLIN
from message import Message

INDEX_NAME = 'name'
INDEX_MESSAGES = 'messages'
INDEX_BUFFER_SIZE = 'buffer_size'
INDEX_FRAME_TIMEOUT = 'frame_timeout'
INDEX_DEBUG = 'debug'

TIMEOUT = 100

class Protocol:
    _start_time = 0

    def __init__(self, json_obj):
        self.name = json_obj[INDEX_NAME]
        self.buffer_size = json_obj[INDEX_BUFFER_SIZE]
        self.frame_timeout = json_obj[INDEX_FRAME_TIMEOUT]
        self.debug = json_obj[INDEX_DEBUG]
        self._poll = poll()
        self._poll.register(sys.stdin, POLLIN)
        self.messages = []
        for json_msg in json_obj[INDEX_MESSAGES]:
            self.messages.append(Message(json_msg))

        self.on_receive_byte = lambda data: None
        self.on_receive_frame = lambda data: None
        self.on_frame_timeout = lambda data: None
        self.on_respond = lambda data: None

    def run(self):
        buffer = bytearray()
        while True:
            if not self._poll.poll(TIMEOUT):
                continue
            if not buffer:
                self._start_time = utime.ticks_ms()
            _byte = bytes(sys.stdin.read(1), 'utf-8')
            self.on_receive_byte(_byte)
            buffer.extend(_byte)
            frametime = utime.ticks_diff(utime.ticks_ms(), self._start_time)
            if frametime >= self.frame_timeout:
                self.on_frame_timeout(buffer)
                buffer = bytearray()
                continue
            for message in self.messages:
                if message.content == buffer:
                    self.on_receive_frame(buffer)
                    buffer = bytearray()
                    if message.response:
                        sys.stdout.write(message.response)
