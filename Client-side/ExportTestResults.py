import csv
import time
import math
import cPickle

# TODO - Write 'Throughput'to file
# TODO - Write 'Percentage of jobs completed' to file
# TODO - Write 'Dropped packets' to file
# TODO - Write 'Faults occurred, by type' to file
# TODO - Write 'Faults recovered from, by type' to file


class ExportTestResults:

    def __init__(self):
        self.name = self
        self.filename = 'test_results/' + time.strftime("%d-%m-%Y--%H-%M-%S") + '.csv'

    @staticmethod
    def get_ping():
        try:
            pickle_file = 'visualizer_cache/latency_data.p'
            # Read data file from cache
            with open(pickle_file, 'rb') as pickle:
                latency = cPickle.load(pickle)

            return latency

        except Exception as e:
            print(e)
            print "No latency data available"
            pass

    # TODO - Implement write_startup_to_file method
    def write_startup_to_file(self):
        with open(self.filename, 'wb') as test_file:
            fieldnames = ['Time', 'Occurrence', 'Ping']
            writer = csv.DictWriter(test_file, fieldnames=fieldnames)

            time_str = time.strftime("%H-%M-%S")

            occurrence_str = 'temp'

            writer.writeheader()
            writer.writerow({'Time': time_str, 'Occurrence': occurrence_str, 'Ping': self.get_ping()})

    # TODO - Implement write_fetch_to_file method
    # TODO - Implement write_fault_to_file method
    # TODO - Implement finish_to_file method
