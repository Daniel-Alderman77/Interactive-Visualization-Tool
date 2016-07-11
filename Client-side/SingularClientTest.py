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

        read_data = ReadData()

        # total_number_of_files_available = rest_client.__call__()[1]
        #
        # while self.get_file_count()["Number of files"] <= total_number_of_files_available:
        #     print "Now attempting to retrieve files"
        #
        try:
            if rest_client.__call__()[0] == True:
                print "Connection is successful"

                print self.get_file_count()["Number of files"]

                if self.get_file_count()["Number of files"]:
                    print "Files have been transferred"
                    read_data.parse_memory_data('data_store/data.xml')
                else:
                    print "Files have not been transferred"

        except:
            print "Server is unavailable"

            if self.get_file_count()["Number of files"] > 0:
                print "Files are available for coldstart prediction"

                memory_data = read_data.parse_memory_data('data_store/data.xml')

                total_memory = int(memory_data[0])
                print total_memory
            else:
                print "Files are not available for coldstart prediction"

startup = Startup()
startup()
