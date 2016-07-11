import glob
import os
import requests
from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError
import json


class RESTClient:

    def __init__(self):
        self.name = self

    def get_request(self):

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

    def get_data(self, argument):
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

    def get_prediction_cache_file_count(self):
        file_count = (len(glob.glob1("data_store", "*.xml")))

        list_of_files = []
        if file_count > 0:
            list_of_files = glob.glob1("data_store", "*.xml")

        return file_count

    def __call__(self):

        try:
            response = self.get_request()

            response_dict = json.loads(response.text)

            number_of_files = 0

            if 'Number of files' in response_dict:
                number_of_files = response_dict['Number of files']
                # print number_of_files

                list_of_files = response_dict['List of files']
                # print list_of_files[0]

                data = self.get_data(list_of_files[0])

                data_store_path = "data_store"

                if not os.path.exists(data_store_path):
                    os.makedirs(data_store_path)

                filename = (list_of_files[0])

                # Encode data into string from unicode
                data_file_contents = data.text.encode('ascii', 'ignore')

                with open(os.path.join(data_store_path, filename), 'wb') as data_file:
                    data_file.write(data_file_contents)

                # Prediction cache
                prediction_cache_path = "prediction_cache"

                # Check if number of files in cache is > 4
                if self.get_prediction_cache_file_count() > 4:
                    print "Greater than 4 files in prediction_cache"

                    if not os.path.exists(prediction_cache_path):
                        os.makedirs(prediction_cache_path)

                    with open(os.path.join(prediction_cache_path, filename), 'wb') as data_file:
                        data_file.write(data_file_contents)

                else:
                    print "Less than 4 files in prediction_cache"

                    if not os.path.exists(prediction_cache_path):
                        os.makedirs(prediction_cache_path)

                    with open(os.path.join(prediction_cache_path, filename), 'wb') as data_file:
                        data_file.write(data_file_contents)

            return True, number_of_files

        except:
            return False
