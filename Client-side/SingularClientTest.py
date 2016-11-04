import shutil

from FileHandler import WebServiceClient, ResponseDeserialization
from Views import UserInterface


# Initial Loop
# TODO - If response is successful, deserialize data, pass data to visualizer
# TODO - Else, cold start prediction, pass data to visualizer
# TODO - Exhaust file call new one

# Repeated Loop
# TODO - If response is successful, deserialize data, pass data to visualizer
# TODO - Else, use prediction
# TODO - Exhaust file call new one
# TODO - Repeat till all files have retrieved from sever-side and rendered to user
class Startup:

    def __init__(self):
        self.name = self

    @staticmethod
    def initial_loop(index):
        web_service_client = WebServiceClient()

        response_deserialization = ResponseDeserialization()

        # Contact server and return number of remote files available
        number_of_remote_files = web_service_client.get_remote_file_count(index)

        print("Number of remote files: %s" % number_of_remote_files)

        web_service_client.calculate_ping()

        # Check file transfer has been successful
        if web_service_client.check_transfer(index):
            list_of_files = web_service_client.get_local_file_count()["List of files"]

            filename = 'data_store/' + list_of_files[index]

            # Deserialize filename passed as a parameter
            # response_deserialization.parse_memory_data(filename)

            response_deserialization.parse_energy_data(filename)
        else:
            print "Now starting cold start prediction"

    def __call__(self):
        user_interface = UserInterface()

        # Start UI
        root = user_interface.run()

        index = 0

        # Start initial loop
        self.initial_loop(index)

        # TODO - Start repeated loop

        # End UI loop
        user_interface.main_loop(root)

        # Deletes data_store directory as app closes
        try:
            shutil.rmtree('data_store')

        except Exception as e:
            print(e)
            print "data_store directory cannot be deleted"
            raise


startup = Startup()
startup()
