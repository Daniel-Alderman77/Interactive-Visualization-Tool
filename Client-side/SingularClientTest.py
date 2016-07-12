import shutil

from FileHandler import WebServiceClient
from Views import UserInterface


# Initial Loop
# TODO - If response is successful, deserialize data, pass data to visualizer
# TODO - Else, coldstart prediction
# TODO - Exhaust file call new one

# Repeated Loop
# TODO - If response is successful, deserialize data, pass data to visualizer
# TODO - Else, use prediction
# TODO - Exhaust file call new one
# TODO - Repeat till all files have retrieved from sever-side and rendered to user
class Startup:

    def __init__(self):
        self.name = self

    def initial_loop(self, index):
        web_service_client = WebServiceClient()

        # Contact server and return number of remote files available
        number_of_remote_files = web_service_client.get_remote_file_count(index)

        print number_of_remote_files

        # Check file transfer has been successful
        if web_service_client.check_transfer(index) == True:
            print True

    def __call__(self):
        user_interface = UserInterface()

        # Start UI
        root = user_interface.run()

        web_service_client = WebServiceClient()

        index = 0

        # Start initial loop
        self.initial_loop(index)

        # TODO - Start repeated loop

        # End UI loop
        user_interface.main_loop(root)

        # Deletes data_store directory as app closes
        try:
            shutil.rmtree('data_store')
        except:
            print "data_store directory cannot be deleted"


startup = Startup()
startup()
