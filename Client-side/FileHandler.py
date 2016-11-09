import glob
import cPickle
import os
from lxml import etree
import requests
from requests.exceptions import ReadTimeout, ConnectionError

from RESTClient import RESTClient
from ExportTestResults import ExportTestResults


class WebServiceClient:

    def __init__(self):
        self.name = self
        self.ping = ""

    @staticmethod
    def get_local_file_count():
        file_count = (len(glob.glob1("data_store", "*.xml")))

        list_of_files = []
        if file_count > 0:
            list_of_files = glob.glob1("data_store", "*.xml")

        return {'Number of files': file_count,
                'List of files': list_of_files}

    @staticmethod
    def get_remote_file_count(index):
        rest_client = RESTClient()

        try:
            if rest_client.read_datafile(index):
                print "Connection is successful"

                number_of_remote_files = rest_client.get_number_of_files()

                return number_of_remote_files

        except Exception as e:
            print(e)
            print "Server is unavailable"
            pass

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

        except Exception as e:
            print(e)
            print "File cannot be transferred"
            pass

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

    @staticmethod
    def parse_cpu_data(filename):
        try:
            cpu_values = []

            tree = etree.parse(filename)
            root = tree.getroot()

            nodes = root[0]
            for node in nodes:
                if node.tag == 'LOG-NODE':
                    log_nodes = node
                    machine_id = node.get('ID')

                    properties = log_nodes.findall('.//Property')

                    for property in properties:
                        if property.get('Name') == 'T_out':
                            cpu_time = property.get('Value')

                            cpu_values.append({machine_id: cpu_time})

            print("CPU Time: %s" % cpu_values)

            # Calculate time stamp
            log_nodes = root.findall('.//LOG-NODE')
            first_log_node = log_nodes[0]
            time_stamp = first_log_node.get('Time')
            print("Time Stamp: %s" % time_stamp)

            cpu_data = [cpu_values, time_stamp]

            pickle_name = 'visualizer_cache/cpu_data.p'

            # Check with pickle exists
            if os.path.isfile(pickle_name):
                # If the pickle exists delete ut
                os.remove(pickle_name)

                # And create new pickle file
                with open(pickle_name, 'wb') as pickle:
                    cPickle.dump(cpu_data, pickle)

            else:
                # If visualizer_cache doesnt't exist create it
                directory = 'visualizer_cache'
                if not os.path.exists(directory):
                    os.makedirs(directory)

                # Pickle data to a new file
                with open(pickle_name, 'wb') as pickle:
                    cPickle.dump(cpu_data, pickle)

        except Exception as e:
            print(e)
            print "No energy data available"
            pass

    @staticmethod
    def parse_memory_data(filename):
        try:
            memory_values = {'node_ID': [], 'memory': []}

            total_memory = 0

            root = etree.parse(filename)

            properties = root.findall('.//Property')

            for property in properties:
                if property.get('Name') == 'ID':
                    node_id = property.get('Value')

                    memory_values['node_ID'].append(node_id)

                if property.get('Name') == 'Memory':
                    memory_value = property.get('Value')

                    memory_values['memory'].append(memory_value)

                    total_memory += int(memory_value)

            print memory_values

            # Calculate total memory usage
            print("Total Memory: %s" % total_memory)

            # Calculate time stamp
            log_nodes = root.findall('.//LOG-NODE')
            first_log_node = log_nodes[0]
            time_stamp = first_log_node.get('Time')

            memory_data = [total_memory, memory_values, time_stamp]

            pickle_name = 'visualizer_cache/memory_data.p'

            # Check with pickle exists
            if os.path.isfile(pickle_name):
                # If the pickle exists delete ut
                os.remove(pickle_name)

                # And create new pickle file
                with open(pickle_name, 'wb') as pickle:
                    cPickle.dump(memory_data, pickle)

            else:
                # If visualizer_cache doesnt't exist create it
                directory = 'visualizer_cache'
                if not os.path.exists(directory):
                    os.makedirs(directory)

                # Pickle data to a new file
                with open(pickle_name, 'wb') as pickle:
                    cPickle.dump(memory_data, pickle)

        except Exception as e:
            print(e)
            print "No memory data available"
            pass

    @staticmethod
    def parse_jobs_data(filename):
        try:
            job_values = []
            total_machines = 0

            tree = etree.parse(filename)
            root = tree.getroot()

            nodes = root[0]
            for node in nodes:
                if node.tag == 'LOG-NODE':
                    log_nodes = node
                    machine_id = node.get('ID')

                    properties = log_nodes.findall('.//Property')

                    for property in properties:
                        if property.get('Name') == 'ID':
                            job_id = property.get('Value')

                            job_values.append({machine_id: job_id})

                    total_machines += 1

            # Calculate total number of machines
            print("Total Number of Machines: %s" % total_machines)

            # Calculate total number of jobs
            total_jobs = len(job_values)
            print("Total Number of Jobs: %s" % total_jobs)

            # Calculate time stamp
            log_nodes = root.findall('.//LOG-NODE')
            first_log_node = log_nodes[0]
            time_stamp = first_log_node.get('Time')

            jobs_data = [total_machines, total_jobs, job_values, time_stamp]

            pickle_name = 'visualizer_cache/jobs_data.p'

            # Check with pickle exists
            if os.path.isfile(pickle_name):
                # If the pickle exists delete ut
                os.remove(pickle_name)

                # And create new pickle file
                with open(pickle_name, 'wb') as pickle:
                    cPickle.dump(jobs_data, pickle)

            else:
                # If visualizer_cache doesnt't exist create it
                directory = 'visualizer_cache'
                if not os.path.exists(directory):
                    os.makedirs(directory)

                # Pickle data to a new file
                with open(pickle_name, 'wb') as pickle:
                    cPickle.dump(jobs_data, pickle)

        except Exception as e:
            print(e)
            print "No energy data available"
            pass

    @staticmethod
    def parse_energy_data(filename):
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

                    total_energy += int(energy_value)

            # Calculate total energy usage
            print("Total Energy: %s" % total_energy)

            # Calculate time stamp
            log_nodes = root.findall('.//LOG-NODE')
            first_log_node = log_nodes[0]
            time_stamp = first_log_node.get('Time')

            energy_data = [total_energy, energy_values, time_stamp]

            pickle_name = 'visualizer_cache/energy_data.p'

            # Check with pickle exists
            if os.path.isfile(pickle_name):
                # If the pickle exists delete ut
                os.remove(pickle_name)

                # And create new pickle file
                with open(pickle_name, 'wb') as pickle:
                    cPickle.dump(energy_data, pickle)

            else:
                # If visualizer_cache doesnt't exist create it
                directory = 'visualizer_cache'
                if not os.path.exists(directory):
                    os.makedirs(directory)

                # Pickle data to a new file
                with open(pickle_name, 'wb') as pickle:
                    cPickle.dump(energy_data, pickle)

        except Exception as e:
            print(e)
            print "No energy data available"
            pass


# TODO - Implement Late-timing fault detection
# TODO - Implement 404 resource not found fault detection
# TODO - Implement 500 internal server error fault detection
class FaultDetection:

    def __init__(self):
        self.name = self
