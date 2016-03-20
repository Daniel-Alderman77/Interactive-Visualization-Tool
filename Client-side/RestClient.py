import requests
from requests.exceptions import ConnectTimeout

class RestClient:

    def __init__(self):
        self.name = self

    def GetRequest(self):

        request = None

        try:
            session = requests.Session()

            request = session.get('http://github.com', timeout = 0.05)

            print(request)

        except ConnectTimeout:
            print "Connection has timed out"

        return request