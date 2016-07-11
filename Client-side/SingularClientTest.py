from FileHandler import ResponseDeserialization, WebServiceClient
from RESTClient import RESTClient


class Startup:

    def __init__(self):
        self.name = self

    def __call__(self):
        request_data = WebServiceClient()

        request_data.request_data()

startup = Startup()
startup()
