import shutil
import threading
import time
import sys
import cPickle

from WebServiceClient import WebServiceClient
from FileHandler import ResponseDeserialization
from Views import UserInterface
from ExportTestResults import ExportTestResults
from RESTClient import RESTClient
from Prediction import DataStore

client_number = 0

# Store command line arguments if present and change test test_file_name
if sys.argv > 1:
    try:
        client_number = sys.argv[2]
    except:
        pass
else:
    print "No command line arguments entered"

visualizer_cache_path = 'visualizer_cache_' + client_number
data_store_path = 'data_store_' + client_number


class Startup:

    def __init__(self):
        self.name = self

        # Create class instances
        self.export_test_results = ExportTestResults()
        self.web_service_client = WebServiceClient()
        self.response_deserialization = ResponseDeserialization()
        self.user_interface = UserInterface()
        self.rest_client = RESTClient()
        self.data_store = DataStore()

    @staticmethod
    def calculate_ping(class_instance):
        # Executes function in background thread
        ping_thread = threading.Thread(target=class_instance.calculate_ping())
        ping_thread.start()

    @staticmethod
    def test_run_cleanup():
        # Delete data_store and visualizer_cache directories
        try:
            shutil.rmtree(data_store_path)
            shutil.rmtree(visualizer_cache_path)
        except Exception as e:
            print e
            pass

    def program_loop(self, index):
        # Create test file
        self.export_test_results.create_test_file()

        # Calculates ping between server and client
        self.calculate_ping(self.web_service_client)

        self.export_test_results.write_startup_to_file()

        # Contact server and return number of remote files available
        number_of_remote_files = self.web_service_client.get_remote_file_count(index)

        print("Number of remote files: %s" % number_of_remote_files)

        # Catch if client cannot establish connection to Server
        while number_of_remote_files is None:
            number_of_remote_files = self.web_service_client.get_remote_file_count(index)

            self.data_store.cold_start_prediction('CPU', 0)
            self.data_store.cold_start_prediction('Memory', 0)
            self.data_store.cold_start_prediction('Jobs', 0)
            self.data_store.cold_start_prediction('Energy', 0)

        while index < number_of_remote_files:
            self.calculate_ping(self.web_service_client)

            pickle_file = visualizer_cache_path + '/latency_data.p'
            # Read data file from cache
            with open(pickle_file, 'rb') as pickle:
                latency = cPickle.load(pickle)

            # Catch if client cannot establish connection to Server, then wait until connection is reestablished
            while latency == 'ConnectionError':
                print 'Attempting to reconnect with Server'

                self.calculate_ping(self.web_service_client)

                pickle_file = visualizer_cache_path + '/latency_data.p'
                # Read data file from cache
                with open(pickle_file, 'rb') as pickle:
                    # When connection is reestablished latency will no longer be 'ConnectionError'
                    latency = cPickle.load(pickle)

            # Check file transfer has been successful
            if self.web_service_client.check_transfer(index):
                try:
                    list_of_files = self.web_service_client.get_local_file_count()["List of files"]

                    self.export_test_results.write_fetch_to_file(list_of_files[index])
                    
                    filename = data_store_path + '/' + list_of_files[index]

                    # Deserialize filename passed as a parameter
                    self.response_deserialization.parse_cpu_data(filename)
                    self.response_deserialization.parse_memory_data(filename)
                    self.response_deserialization.parse_jobs_data(filename)
                    self.response_deserialization.parse_energy_data(filename)

                    # Increment index
                    index += 1

                    # Retrieve new file
                    self.rest_client.read_datafile(index)

                except Exception as e:
                    print e
                    raise

            # Make thread sleep for one second
            time.sleep(1)

        print "Exhausted all files on the server"

        self.export_test_results.write_finish_to_file()

        print "Cleaning test environment..."
        self.test_run_cleanup()

        # End UI loop
        self.user_interface.destroy()

        # End program
        sys.exit(1)

    def main(self, index):
        # Executes function in background thread
        main_thread = threading.Thread(target=self.program_loop, args=[index])
        main_thread.start()

    def __call__(self):
        # Start UI
        root = self.user_interface.run()

        # File local datafile index. Increments as each new file is visualized
        index = 0

        # Start program loop
        self.main(index)

        root.mainloop()

startup = Startup()
startup()
