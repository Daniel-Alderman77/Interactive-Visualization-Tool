from FileHandler import WebServiceClient


# Initial Loop
# TODO - Display UI
# TODO - Client contacts server
# TODO - If response is successful, deserialise data, pass data to visualizer
# TODO - Else, coldstart prediction
# TODO - Exhaust file call new one

# Repeated Loop
# TODO - Client contacts server
# TODO - If response is successful, deserialise data, pass data to visualizer
# TODO - Else, use prediction
# TODO - Exhaust file call new one
# TODO - Repeat till all files have retrieved from sever-side and rendered to user
class Startup:

    def __init__(self):
        self.name = self

    def __call__(self):
        request_data = WebServiceClient()

        request_data.request_data()

startup = Startup()
startup()
