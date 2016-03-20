import requests

class RestClient:

    def __init__(self):
        self.name = self

    def GetRequest(self):
        session = requests.Session()

        request = session.get('http://github.com', timeout = 0.05)

        print(request)

        return request