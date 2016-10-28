import glob
from lxml import etree
import requests
from requests.exceptions import ReadTimeout, ConnectionError

from RESTClient import RESTClient
from ExportTestResults import ExportTestResults


class WebServiceClient:

    def __init__(self):
        self.name = self
        self.ping = ""

    def get_local_file_count(self):
        file_count = (len(glob.glob1("data_store", "*.xml")))

        list_of_files = []
        if file_count > 0:
            list_of_files = glob.glob1("data_store", "*.xml")

        return {'Number of files': file_count,
                'List of files': list_of_files}

    def get_remote_file_count(self, index):
        rest_client = RESTClient()

        try:
            if rest_client.read_datafile(index) == True:
                print "Connection is successful"

                number_of_remote_files = rest_client.get_number_of_files()

                return number_of_remote_files
        except:
            print "Server is unavailable"

    def check_transfer(self, index):
        try:
            number_of_files = self.get_local_file_count()["Number of files"]

            print("Number of local files: %s" % number_of_files)

            if index == (number_of_files - 1):
                print "File has been transferred"

                return True
            else:
                print "File has not been transferred"

                return False

        except:
            print "File cannot be transferred"

            return False

    def calculate_ping(self):
        export_test_results = ExportTestResults()

        try:
            session = requests.Session()

            request = session.get('http://127.0.0.1:5000/')

            self.ping = request.elapsed

            print 'Ping = ', self.ping

            export_test_results.write_to_file(self.ping)

        except ReadTimeout:
            print "Connection has timed out"

            self.ping = "ReadTimeout"

            export_test_results.write_to_file(self.ping)

        except ConnectionError:
            print "Failed to establish connection to Server"

            self.ping = "ConnectionError"

            export_test_results.write_to_file(self.ping)


class ResponseDeserialization:

    def __init__(self):
        self.name = self
        self.energy_visualizer_data = []

    def get_energy_visualizer_data(self):
        return self.energy_visualizer_data

    def set_energy_visualizer_data(self, parameters):
        self.energy_visualizer_data = parameters

    def parse_memory_data(self, filename):
        try:
            total_memory = None
            task1 = None
            task2 = None

            root = etree.parse(filename)

            log_node = root.find('.//LOG-NODE')
            log_node_contents = log_node.getchildren()
            for content in log_node_contents:
                if content.get('Name') == 'Memory':
                    total_memory = content.get('Value')

            actions = root.findall('.//LOG-ACTION')

            # TODO - Implement for loop to search for values based on number nodes in file

            log_action_contents = actions[0].getchildren()
            for content in log_action_contents:
                if content.get('Name') == 'Memory_Allocated':
                    task1 = content.get('Value')

            log_action_contents = actions[1].getchildren()
            for content in log_action_contents:
                if content.get('Name') == 'Memory_Allocated':
                    task2 = content.get('Value')

            print("Total Memory: %s" % total_memory)

            print("Task 1 Memory: %s" % task1)

            print("Task 2 Memory: %s" % task2)

            return [total_memory, task1, task2]
        except:
            print "No memory data available"

    def parse_energy_data(self, filename):
        try:
            energy_values = {'node_ID': [], 'energy': []}

            total_energy = 0

            root = etree.parse(filename)

            properties = root.findall('.//Property')

            for property in properties:
                if property.get('Name') == 'ID':
                    node_id = property.get('Value')

                    energy_values['node_ID'].append(node_id)

                if property.get('Name') == 'Energy':
                    energy_value = property.get('Value')

                    energy_values['energy'].append(energy_value)

                    total_energy = int(energy_value) + total_energy

            # print len(energy_values)
            #
            # print energy_values
            #
            # print energy_values['node_ID'][0]
            #
            # print energy_values['energy'][0]

            # Calculate total energy usage
            print("Total Energy: %s" % total_energy)

            log_nodes = root.findall('.//LOG-NODE')

            first_log_node = log_nodes[0]

            time_stamp = first_log_node.get('Time')

            print("Time Stamp: %s" % time_stamp)

            parameters = [total_energy, energy_values, time_stamp]

            self.set_energy_visualizer_data(parameters)

            print self.get_energy_visualizer_data()

        except:
            print "No energy data available"


# TODO - Implement Late-timing fault detection
# TODO - Implement 404 resource not found fault detection
# TODO - Implement 500 internal server error fault detection
class FaultDetection:

    def __init__(self):
        self.name = self
