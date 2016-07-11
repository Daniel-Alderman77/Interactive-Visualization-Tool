from FileHandler import ResponseDeserialization, WebServiceClient
from RESTClient import RESTClient


class Startup:

    def __init__(self):
        self.name = self

    def __call__(self):
        rest_client = RESTClient()

        read_data = ResponseDeserialization()

        request_data = WebServiceClient()

        # total_number_of_files_available = rest_client.__call__()[1]
        #
        # while self.get_file_count()["Number of files"] <= total_number_of_files_available:
        #     print "Now attempting to retrieve files"
        #

        request_data.request_data()

startup = Startup()
startup()
