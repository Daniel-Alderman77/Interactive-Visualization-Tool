from __future__ import division
import csv
import os
import time
import cPickle
from collections import defaultdict
import sys

client_number = 0
run_number = 0
test_file_name = 'test_results/' + time.strftime("%d-%m-%Y--%H:%M:%S") + '.csv'
faults = 0

# Store command line arguments if present and change test test_file_name
if sys.argv > 1:
    try:
        client_number = "client_" + sys.argv[1]
        run_number = "run_number" + sys.argv[2]
        test_file_name = 'test_results/' + str(run_number) + '/' + str(client_number) + '/' + time.strftime(
            "%d-%m-%Y--%H:%M:%S") + '.csv'

    except:
        pass
else:
    print "No command line arguments entered"


class ExportTestResults:
    number_of_faults = 0

    def __init__(self):
        self.name = self
        self.fieldnames = ['Time', 'Occurrence', 'Ping']
        self.start_time = time.time()

        self.number_jobs_completed = 0
        self.faults_occurred = defaultdict(int)

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

        if run_number and client_number != 0:
            test_results_path = "test_results" + "/" + str(run_number) + "/" + str(client_number)

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

                self.number_jobs_completed += 1

                writer.writerow({'Time': time_str, 'Occurrence': occurrence_str, 'Ping': self.get_ping()})

        except Exception as e:
            print e

    def write_fault_to_file(self, fault):
        try:
            with open(test_file_name, 'a') as test_file:
                writer = csv.DictWriter(test_file, fieldnames=self.fieldnames)

                time_str = time.strftime("%H:%M:%S")

                occurrence_str = fault + ' fault has occurred'

                self.faults_occurred[fault] += 1

                self.increment_number_of_faults()

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

    @staticmethod
    def increment_number_of_faults():
        global faults
        faults += 1

        return faults

    # TODO - Implement write_finish_to_file method
    def write_finish_to_file(self):
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

                print("Time Elapsed = %s" % time_elapsed)

                # Write time elapsed
                writer.writerow({'Time': 'Time Elapsed (seconds)', 'Occurrence': str(time_elapsed)})

                number_of_faults = (self.increment_number_of_faults() - 1)
                print("Number of faults = %s" % number_of_faults)
                print("Number of jobs complete = %s" % self.number_jobs_completed)

                percentage_of_jobs_failed = (number_of_faults / self.number_jobs_completed) * 100
                percentage_of_jobs_completed = 100 - round(percentage_of_jobs_failed, 2)
                print("Percentage of jobs completed = %s" % percentage_of_jobs_completed)

                # Write time elapsed
                writer.writerow({'Time': 'Percentage of jobs completed', 'Occurrence': percentage_of_jobs_completed})

                throughput = round((self.number_jobs_completed / time_elapsed), 2)
                print("Throughput (per second) = %s" % throughput)

                # Write throughput
                writer.writerow({'Time': 'Throughput (per second)', 'Occurrence': throughput})

                # # TODO - Write 'Faults occurred, by type' to file
                # # Write 'Faults occurred, by type' to file
                # for key, value in self.faults_occurred.iteritems():
                #     writer.writerow({'Time': 'Fault Type: ' + key, 'Occurrence': value})

                # TODO - Write 'Faults recovered from, by type' to file

        except Exception as e:
            print e