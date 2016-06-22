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

            print(request.status_code)

            print(request.text)

            # Time elapsed between sending the request and arrival of response
            print(request.elapsed)

        except ReadTimeout:
            print "Connection has timed out"

        except ConnectionError:
            print "Failed to establish connection to Server"

        return request

    def get_data(self):
        print ("")

    def __call__(self):
        response = self.get_request()

        response_dict = json.loads(response.text)

        if 'Number of files' in response_dict:
            number_of_files = response_dict['Number of files']
            print number_of_files

        self.get_data()

client = RESTClient()
client()
