import os
import requests
from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError
import json

from Prediction import DataStore


class RESTClient:

    def __init__(self):
        self.name = self

    def get_number_of_files(self):
        return self.number_of_files

    def set_number_of_files(self, x):
        self.number_of_files = x

    def get_file_count(self):

        request = None

        try:
            session = requests.Session()

            request = session.get('http://127.0.0.1:5000/file_count/', timeout=0.1)

            # print(request.status_code)

            # print(request.text)

            # Time elapsed between sending the request and arrival of response
            # print(request.elapsed)

        except ReadTimeout:
            print "Connection has timed out"

        except ConnectionError:
            print "Failed to establish connection to Server"

        return request

    def get_datafile(self, argument):
        request = None

        try:
            session = requests.Session()

            path = 'http://127.0.0.1:5000/data/' + argument

            request = session.get(path, timeout=0.1)

            # print(request.status_code)

            # print(request.text)

            # Time elapsed between sending the request and arrival of response
            # print(request.elapsed)

        except ReadTimeout:
            print "Connection has timed out"

        except ConnectionError:
            print "Failed to establish connection to Server"

        return request

    # TODO - Refactor __call__ method, to be called programmatically
    def __call__(self):
        try:
            response = self.get_file_count()

            response_dict = json.loads(response.text)

            number_of_files = 0

            if 'Number of files' in response_dict:
                number_of_files = response_dict['Number of files']
                # print number_of_files

                list_of_files = response_dict['List of files']
                # print list_of_files[0]

                data = self.get_datafile(list_of_files[0])

                data_store_path = "data_store"

                if not os.path.exists(data_store_path):
                    os.makedirs(data_store_path)

                filename = (list_of_files[0])

                # Encode data into string from unicode
                data_file_contents = data.text.encode('ascii', 'ignore')

                with open(os.path.join(data_store_path, filename), 'wb') as data_file:
                    data_file.write(data_file_contents)

                # Prediction
                data_store = DataStore()

                data_store.prediction_cache(filename, data_file_contents)

                self.set_number_of_files(number_of_files)

            return True

        except:
            return False
