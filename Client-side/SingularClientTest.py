from FileHandler import ReadData, RequestData
from RESTClient import RESTClient


class Startup:

    def __init__(self):
        self.name = self

    def __call__(self):
        rest_client = RESTClient()

        read_data = ReadData()

        request_data = RequestData()

        # total_number_of_files_available = rest_client.__call__()[1]
        #
        # while self.get_file_count()["Number of files"] <= total_number_of_files_available:
        #     print "Now attempting to retrieve files"
        #

        request_data.request_data()

startup = Startup()
startup()
