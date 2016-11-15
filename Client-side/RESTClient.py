import os
import requests
from requests.exceptions import ReadTimeout, ConnectionError, HTTPError
import json

from Prediction import DataStore
from FaultDetection import FaultDetection


class RESTClient:

    def __init__(self):
        self.name = self
        self.data_store = DataStore()

    def get_number_of_files(self):
        return self.number_of_files

    def set_number_of_files(self, file):
        self.number_of_files = file

    def get_list_of_files(self):
        return self.list_of_files

    def set_list_of_files(self, list):
        self.list_of_files = list

    @staticmethod
    def get_file_count():
        fault_detection = FaultDetection()

        request = None

        try:
            session = requests.Session()

            request = session.get('http://127.0.0.1:5000/file_count/', timeout=0.1)

            request.raise_for_status()

        except HTTPError as error:
            print error
            fault_detection.http_error(error)

        except ReadTimeout:
            print "Connection has timed out"
            fault_detection.late_timing_fault()

        except ConnectionError:
            print "Failed to establish connection to Server"
            fault_detection.connection_error()

        return request

    @staticmethod
    def get_datafile(argument):
        fault_detection = FaultDetection()

        request = None

        try:
            session = requests.Session()

            path = 'http://127.0.0.1:5000/data/' + argument

            request = session.get(path, timeout=0.1)

        except HTTPError as error:
            print error
            fault_detection.http_error(error)

        except ReadTimeout:
            print "Connection has timed out"
            fault_detection.late_timing_fault()

        except ConnectionError:
            print "Failed to establish connection to Server"
            fault_detection.connection_error()

        return request

    def read_datafile(self, index):
        try:
            response = self.get_file_count()

            response_dict = json.loads(response.text)

            if 'Number of files' in response_dict:
                number_of_files = response_dict['Number of files']

                list_of_files = response_dict['List of files']

                data = self.get_datafile(list_of_files[index])

                data_store_path = "data_store"

                if not os.path.exists(data_store_path):
                    os.makedirs(data_store_path)

                filename = (list_of_files[0])

                # Encode data into string from unicode
                data_file_contents = data.text.encode('ascii', 'ignore')

                with open(os.path.join(data_store_path, filename), 'wb') as data_file:
                    data_file.write(data_file_contents)

                # Write file to prediction cache
                self.data_store.prediction_cache(filename, data_file_contents)

                self.set_number_of_files(number_of_files)

                self.set_list_of_files(list_of_files)

            return True

        except Exception as e:
            print(e)
            return False
