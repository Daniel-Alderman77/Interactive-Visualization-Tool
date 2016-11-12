import csv
import time
import cPickle

# TODO - Write 'Throughput'to file
# TODO - Write 'Percentage of jobs completed' to file
# TODO - Write 'Dropped packets' to file
# TODO - Write 'Faults occurred, by type' to file
# TODO - Write 'Faults recovered from, by type' to file


class ExportTestResults:

    def __init__(self):
        self.name = self
        self.filename = 'test_results/' + time.strftime("%d-%m-%Y--%H:%M:%S") + '.csv'
        self.fieldnames = ['Time', 'Occurrence', 'Ping']
        self.time_str = time.strftime("%H:%M:%S")

    def get_ping(self):
        try:
            pickle_file = 'visualizer_cache/latency_data.p'
            # Read data file from cache
            with open(pickle_file, 'rb') as pickle:
                latency = cPickle.load(pickle)

            return latency

        except Exception:
            print "No latency data available"
            self.write_fault_to_file('Null Value')
            pass

    def create_test_file(self):
        try:
            with open(self.filename, 'wb') as test_file:
                writer = csv.DictWriter(test_file, fieldnames=self.fieldnames)

                writer.writeheader()
        except Exception as e:
            print e

    def write_startup_to_file(self):
        try:
            with open(self.filename, 'a') as test_file:
                writer = csv.DictWriter(test_file, fieldnames=self.fieldnames)

                occurrence_str = 'Startup'

                writer.writerow(writer.writerow({'Time': self.time_str, 'Occurrence': occurrence_str,
                                                 'Ping': self.get_ping()}))

        except Exception as e:
            print e

    # TODO - Implement write_fetch_to_file method

    def write_fault_to_file(self, fault):
        try:
            with open(self.filename, 'a') as test_file:
                writer = csv.DictWriter(test_file, fieldnames=self.fieldnames)

                occurrence_str = fault + ' fault has occurred'

                writer.writerow(writer.writerow({'Time': self.time_str, 'Occurrence': occurrence_str,
                                                 'Ping': self.get_ping()}))

        except Exception as e:
            print e

    # TODO - Implement finish_to_file method
