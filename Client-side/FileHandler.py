import glob
from lxml import etree

from RESTClient import RESTClient
from Prediction import DataStore


class WebServiceClient:

    def __init__(self):
        self.name = self

    def get_local_file_count(self):
        file_count = (len(glob.glob1("data_store", "*.xml")))

        list_of_files = []
        if file_count > 0:
            list_of_files = glob.glob1("data_store", "*.xml")

        return {'Number of files': file_count,
                'List of files': list_of_files}
    
    def get_remote_file_count(self):
        rest_client = RESTClient()

        try:
            if rest_client.read_datafile() == True:
                print "Connection is successful"

                number_of_remote_files = rest_client.get_number_of_files()

                return number_of_remote_files
        except:
            print "Server is unavailable"

    def check_transfer(self):
        read_data = ResponseDeserialization()

        data_store = DataStore()

        try:
            number_of_files = self.get_local_file_count()["Number of files"]

            print number_of_files

            if number_of_files:
                print "File has been transferred"
                read_data.parse_memory_data('data_store/data.xml')
            else:
                print "File has not been transferred"

        except:
            print "File cannot be transferred"

            data_store.coldstart_prediction()


class ResponseDeserialization:

    def __init__(self):
        self.name = self

    def parse_memory_data(self, filename):
        total_memory = None
        task1 = None
        task2 = None

        root = etree.parse(filename)

        log_node = root.find('.//LOG-NODE')
        log_node_contents = log_node.getchildren()
        for content in log_node_contents:
            if content.get('Name') == 'Memory':
                total_memory = content.get('Value')

        print("Total Memory: %s" % total_memory)

        actions = root.findall('.//LOG-ACTION')

        log_action_contents = actions[0].getchildren()
        for content in log_action_contents:
            if content.get('Name') == 'Memory_Allocated':
                task1 = content.get('Value')

        print("Task 1 Memory: %s" % task1)

        log_action_contents = actions[1].getchildren()
        for content in log_action_contents:
            if content.get('Name') == 'Memory_Allocated':
                task2 = content.get('Value')

        print("Task 2 Memory: %s" % task2)

        return [total_memory, task1, task2]


# TODO - Implement Late-timing fault detection
# TODO - Implement 404 resource not found fault detection
# TODO - Implement 500 internal server error fault detection
class FaultDetection:

    def __init__(self):
        self.name = self
