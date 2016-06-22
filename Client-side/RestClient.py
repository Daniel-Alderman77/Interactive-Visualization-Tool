import requests
from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError


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

    def __call__(self):
        self.get_request()

client = RESTClient()
client()
