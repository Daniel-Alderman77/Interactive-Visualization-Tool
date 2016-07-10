import glob
from FileHandler import ReadData
from RESTClient import RESTClient


class Startup:

    def __init__(self):
        self.name = self

    def get_file_count(self):
        file_count = (len(glob.glob1("data_store", "*.xml")))

        list_of_files = []
        if file_count > 0:
            list_of_files = glob.glob1("data_store", "*.xml")

        return {'Number of files': file_count,
                'List of files': list_of_files}

    def __call__(self):
        rest_client = RESTClient()
        rest_client()

        if rest_client.__call__() == True:
            print "Connection is successful"
        else:
            print "Server is unavailable"

            if self.get_file_count()["Number of files"] > 0:
                print "Files are available for coldstart prediction"

                read_data = ReadData()
                memory_data = read_data.parse_xml('data_store/data.xml')

                total_memory = int(memory_data[0])
                print total_memory
            else:
                print "Files are not available for coldstart prediction"

startup = Startup()
startup()
