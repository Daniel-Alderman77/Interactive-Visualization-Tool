import requests
from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError

class RestClient:

    def __init__(self):
        self.name = self

    def GetRequest(self):

        request = None

        try:
            session = requests.Session()

            request = session.put('http://127.0.0.1:8080/', params={'another_string': 'hello'})

            request = session.get('http://127.0.0.1:8080/', timeout = 0.1)

            print(request.status_code)

            print(request.text)

            # Time elapsed between sending the request and arrival of response
            print(request.elapsed)

        except ReadTimeout:
            print "Connection has timed out"

        except ConnectionError:
            print "Failed to establish connection to Server"

        return request