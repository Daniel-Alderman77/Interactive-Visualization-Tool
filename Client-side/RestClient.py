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

    def __call__(self):

        try:
            response = self.get_request()

            response_dict = json.loads(response.text)

            if 'Number of files' in response_dict:
                number_of_files = response_dict['Number of files']
                # print number_of_files

                list_of_files = response_dict['List of files']
                # print list_of_files[0]

                data = self.get_data(list_of_files[0])

                path = "data_store"

                if not os.path.exists(path):
                    os.makedirs(path)

                filename = (list_of_files[0])

                # Encode data into string from unicode
                data_file_contents = data.text.encode('ascii', 'ignore')

                with open(os.path.join(path, filename), 'wb') as data_file:
                    data_file.write(data_file_contents)
            return True

        except:
            return False

client = RESTClient()
client()
