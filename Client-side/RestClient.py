import requests
from requests.exceptions import ConnectTimeout

class RestClient:

    def __init__(self):
        self.name = self

    def GetRequest(self):

        request = None

        try:
            session = requests.Session()

            request = session.put('http://127.0.0.1:8080/', params={'another_string': 'hello'})

            request = session.get('http://127.0.0.1:8080/', timeout = 0.05)

            print(request.status_code)

            print(request.text)

        except ConnectTimeout:
            print "Connection has timed out"

        return request