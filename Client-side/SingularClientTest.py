import glob
import os
import threading
import time

from WebServiceClient import WebServiceClient
from FileHandler import ResponseDeserialization
from Views import UserInterface
from ExportTestResults import ExportTestResults


# Initial Loop
# TODO - Exhaust file call new one

# Repeated Loop
# TODO - If response is successful, deserialize data, pass data to visualizer
# TODO - Else, use prediction
# TODO - Exhaust file call new one
# TODO - Repeat till all files have retrieved from sever-side and rendered to user

class Startup:

    def __init__(self):
        self.name = self

        # Create class instances
        self.export_test_results = ExportTestResults()
        self.web_service_client = WebServiceClient()
        self.response_deserialization = ResponseDeserialization()
        self.user_interface = UserInterface()

    @staticmethod
    def calculate_ping(class_instance):
        # Executes function in background thread
        ping_thread = threading.Thread(target=class_instance.calculate_ping())
        ping_thread.start()

    @staticmethod
    def test_run_cleanup():
        # Load filenames in data_store in array
        data_store = glob.glob1("data_store", "*.xml")

        # Deletes each file named in the list
        for data_file in data_store:
            try:
                os.remove(data_file)
            except OSError:
                pass

    def program_loop(self, index):

        # Calls function that continuously calculates ping
        self.calculate_ping(self.web_service_client)

        self.export_test_results.create_test_file()

        self.export_test_results.write_startup_to_file()

        # Contact server and return number of remote files available
        number_of_remote_files = self.web_service_client.get_remote_file_count(index)

        number_of_local_files = self.web_service_client.get_local_file_count()['Number of files']

        print("Number of remote files: %s" % number_of_remote_files)

        while number_of_remote_files < number_of_local_files:
            # Check file transfer has been successful
            if self.web_service_client.check_transfer(index):
                list_of_files = self.web_service_client.get_local_file_count()["List of files"]

                self.export_test_results.write_fetch_to_file(list_of_files[index])

                filename = 'data_store/' + list_of_files[index]

                # Deserialize filename passed as a parameter
                self.response_deserialization.parse_cpu_data(filename)
                self.response_deserialization.parse_memory_data(filename)
                self.response_deserialization.parse_jobs_data(filename)
                self.response_deserialization.parse_energy_data(filename)

                time.sleep(1)

    def main(self, index):
        # Executes function in background thread
        main_thread = threading.Thread(target=self.program_loop, args=[index])
        main_thread.start()

    def __call__(self):
        # Start UI
        root = self.user_interface.run()

        # File local datafile index. Incremets as each new file is visualized
        index = 0

        # Start initial loop
        self.main(index)

        # TODO - Start repeated loop

        # End UI loop
        self.user_interface.main_loop(root)

        self.test_run_cleanup()


startup = Startup()
startup()
