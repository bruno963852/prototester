import ubinascii

INDEX_TYPE = "message_type"
INDEX_CONTENT = "message_content"
INDEX_RESPONSE = "response"
INDEX_RESPONSE_TIME = "response_time"

class Message:
    def __init__(self, json_msg):
        _type = json_msg[INDEX_TYPE]
        self.content = None
        self.response = None

        if _type == MessageType.HEX:
            self.content = ubinascii.unhexlify(json_msg[INDEX_CONTENT])
            self.response = ubinascii.unhexlify(json_msg[INDEX_RESPONSE])
        elif _type == MessageType.ASCII:
            self.content = bytes(json_msg[INDEX_CONTENT], "utf-8")
            self.response = bytes(json_msg[INDEX_RESPONSE], "utf-8")
        else:
            raise ValueError("Wrong Message Type")

        self.type = _type
        self.response_time = json_msg[INDEX_RESPONSE_TIME]

class MessageType:
    HEX = 'hex'
    ASCII = 'ascii'
