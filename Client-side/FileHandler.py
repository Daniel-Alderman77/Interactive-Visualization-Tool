import cPickle
import os
from lxml import etree

from FaultDetection import FaultDetection


class ResponseDeserialization:

    def __init__(self):
        self.name = self

        # Create FaultDetection() instance
        self.fault_detection = FaultDetection()

    def parse_cpu_data(self, filename):
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

        except Exception:
            print "No CPU data available"
            self.fault_detection.null_values_fault('CPU')
            pass

    def parse_memory_data(self, filename):
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

            # print memory_values

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

        except Exception:
            print "No Memory data available"
            self.fault_detection.null_values_fault('Memory')
            pass

    def parse_jobs_data(self, filename):
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

        except Exception:
            print "No Jobs data available"
            self.fault_detection.null_values_fault('Jobs')
            pass

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

        except Exception:
            print "No Energy data available"
            self.fault_detection.null_values_fault('Energy')
            pass
