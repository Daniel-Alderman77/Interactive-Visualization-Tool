import glob
import os
import threading

from WebServiceClient import WebServiceClient
from FileHandler import ResponseDeserialization
from Views import UserInterface
from ExportTestResults import ExportTestResults


# Initial Loop
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
    def calculate_ping(class_instance):
        # Executes function in background thread
        ping_thread = threading.Thread(target=class_instance.calculate_ping())
        ping_thread.start()

    def initial_loop(self, index):
        # Create class instances
        export_test_results = ExportTestResults()
        web_service_client = WebServiceClient()
        response_deserialization = ResponseDeserialization()

        # Calls function that continuously calculates ping
        self.calculate_ping(web_service_client)

        export_test_results.create_test_file()

        export_test_results.write_startup_to_file()

        # Contact server and return number of remote files available
        number_of_remote_files = web_service_client.get_remote_file_count(index)

        print("Number of remote files: %s" % number_of_remote_files)

        # Check file transfer has been successful
        if web_service_client.check_transfer(index):
            list_of_files = web_service_client.get_local_file_count()["List of files"]

            export_test_results.write_fetch_to_file(list_of_files[index])

            filename = 'data_store/' + list_of_files[index]

            # Deserialize filename passed as a parameter
            response_deserialization.parse_cpu_data(filename)
            response_deserialization.parse_memory_data(filename)
            response_deserialization.parse_jobs_data(filename)
            response_deserialization.parse_energy_data(filename)

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

        # Load filenames in data_store in array
        data_store = glob.glob1("data_store", "*.xml")

        # Remove last element so this file can be used for cold start prediction
        data_store.pop([-1])

        # Deletes each file named in the list
        for data_file in data_store:
            try:
                os.remove(data_file)
            except OSError:
                pass


startup = Startup()
startup()
