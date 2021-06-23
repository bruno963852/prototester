from statemachine.statemachine import StateMachine

StateMachine().run()


# import ujson
# import ubinascii
# from view.start_screen import StartScreen
# from protocol import Protocol

# StartScreen().show()

# file = open('example_protocol.json')
# json_obj = ujson.load(file)
# file.close()

# protocol = Protocol(json_obj)

# for _msg in protocol.messages:
#     print("Message: {}".format(_msg.content))

# protocol.run()
