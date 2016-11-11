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

            # Convert latency from timedelta object to seconds. Then round up to the nearest second
            ping = math.ceil(latency.total_seconds())

            return ping

        except Exception as e:
            print(e)
            print "No latency data available"
            pass

    # TODO - Implement write_startup_to_file method
    def write_startup_to_file(self):
        ping = self.get_ping()

        with open(self.filename, 'wb') as test_file:
            fieldnames = ['time', 'ping']
            writer = csv.DictWriter(test_file, fieldnames=fieldnames)

            time_str = time.strftime("%H-%M-%S")

            writer.writeheader()
            writer.writerow({'time': time_str, 'ping': ping})

    # TODO - Implement write_fetch_to_file method
    # TODO - Implement write_fault_to_file method
    # TODO - Implement finish_to_file method

    @staticmethod
    def write_to_file(ping):
        date_time_str = time.strftime("%d-%m-%Y--%H-%M-%S")

        with open('test_results/' + date_time_str + '.csv', 'wb') as test_file:
            fieldnames = ['time', 'ping']
            writer = csv.DictWriter(test_file, fieldnames=fieldnames)

            time_str = time.strftime("%H-%M-%S")

            writer.writeheader()
            writer.writerow({'time': time_str, 'ping': ping})
