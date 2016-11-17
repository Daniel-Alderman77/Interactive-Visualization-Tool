import csv
import os
import time
import cPickle

test_file_name = 'test_results/' + time.strftime("%d-%m-%Y--%H:%M:%S") + '.csv'


class ExportTestResults:

    def __init__(self):
        self.name = self
        self.fieldnames = ['Time', 'Occurrence', 'Ping']
        self.start_time = time.time()

    def get_ping(self):
        try:
            pickle_file = 'visualizer_cache/latency_data.p'
            # Read data file from cache
            with open(pickle_file, 'rb') as pickle:
                latency = cPickle.load(pickle)

            return latency

        except Exception:
            print "No latency data available"
            self.write_fault_to_file('Latency Null Value')
            pass

    def create_test_file(self):
        test_results_path = "test_results"

        try:
            # If test_results directory doesn't exist create it
            if not os.path.exists(test_results_path):
                os.makedirs(test_results_path)

            with open(test_file_name, 'wb') as test_file:
                writer = csv.DictWriter(test_file, fieldnames=self.fieldnames)

                writer.writeheader()

        except Exception as e:
            print e

    def write_startup_to_file(self):
        try:
            with open(test_file_name, 'a') as test_file:
                writer = csv.DictWriter(test_file, fieldnames=self.fieldnames)

                time_str = time.strftime("%H:%M:%S")

                occurrence_str = 'Startup'

                writer.writerow({'Time': time_str, 'Occurrence': occurrence_str, 'Ping': self.get_ping()})

        except Exception as e:
            print e

    def write_fetch_to_file(self, filename):
        try:
            with open(test_file_name, 'a') as test_file:
                writer = csv.DictWriter(test_file, fieldnames=self.fieldnames)

                time_str = time.strftime("%H:%M:%S")

                occurrence_str = filename + ' has been retrieved'

                writer.writerow({'Time': time_str, 'Occurrence': occurrence_str, 'Ping': self.get_ping()})

        except Exception as e:
            print e

    def write_fault_to_file(self, fault):
        try:
            with open(test_file_name, 'a') as test_file:
                writer = csv.DictWriter(test_file, fieldnames=self.fieldnames)

                time_str = time.strftime("%H:%M:%S")

                occurrence_str = fault + ' fault has occurred'

                writer.writerow({'Time': time_str, 'Occurrence': occurrence_str, 'Ping': self.get_ping()})

        except Exception as e:
            print e

    def write_predicted_value_to_file(self, value, type_of_data):
        try:
            with open(test_file_name, 'a') as test_file:
                writer = csv.DictWriter(test_file, fieldnames=self.fieldnames)

                time_str = time.strftime("%H:%M:%S")

                occurrence_str = str(value) + ' has been predicted for ' + type_of_data

                writer.writerow({'Time': time_str, 'Occurrence': occurrence_str, 'Ping': self.get_ping()})

        except Exception as e:
            print e

    # TODO - Implement write_finish_to_file method
    def write_finish_to_file(self):
        # TODO - Write 'Throughput'to file
        # TODO - Write 'Percentage of jobs completed' to file
        # TODO - Write 'Dropped packets' to file
        # TODO - Write 'Faults occurred, by type' to file
        # TODO - Write 'Faults recovered from, by type' to file

        try:
            with open(test_file_name, 'ab') as test_file:
                writer = csv.DictWriter(test_file, fieldnames=self.fieldnames)

                # Write blank row
                writer.writerow({})

                # Write Test Run Summary
                writer.writerow({'Time': 'Test Run Summary'})

                end_time = time.time()
                time_elapsed = end_time - self.start_time

                # Round time_elapsed to two decimal places
                time_elapsed = round(time_elapsed, 2)

                print("Time elapsed = %s" % time_elapsed)

                # Write time elapsed
                writer.writerow({'Time': 'Time elapsed = ' + str(time_elapsed) + ' seconds', 'Occurrence': ''})

        except Exception as e:
            print e
