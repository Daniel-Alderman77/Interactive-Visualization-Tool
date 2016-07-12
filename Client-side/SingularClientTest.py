from FileHandler import WebServiceClient
from Views import UserInterface


# Initial Loop
# TODO - If response is successful, deserialize data, pass data to visualizer
# TODO - Else, coldstart prediction
# TODO - Exhaust file call new one

# Repeated Loop
# TODO - Client contacts server
# TODO - If response is successful, deserialize data, pass data to visualizer
# TODO - Else, use prediction
# TODO - Exhaust file call new one
# TODO - Repeat till all files have retrieved from sever-side and rendered to user
# TODO - As application exits cleanup environment, delete all data from data_store
class Startup:

    def __init__(self):
        self.name = self

    def __call__(self):
        user_interface = UserInterface()

        # Start UI
        root = user_interface.run()

        web_service_client = WebServiceClient()

        web_service_client.get_remote_file_count()

        # End UI loop
        user_interface.main_loop(root)

startup = Startup()
startup()
