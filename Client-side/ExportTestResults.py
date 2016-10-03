import csv
import time

# TODO - Write 'Throughput'to file
# TODO - Write 'Percentage of jobs completed' to file
# TODO - Write 'Dropped packets' to file
# TODO - Write 'Faults occurred, by type' to file
# TODO - Write 'Faults recovered from, by type' to file
# TODO - Write 'Ping' to file


class ExportTestResults:

    def __init__(self):
        self.name = self

    def write_to_file(self):
        date_time_str = time.strftime("%d-%m-%Y--%H-%M-%S")

        with open('test_results/' + date_time_str + '.csv', 'wb') as test_file:
            fieldnames = ['time', 'last_name']
            writer = csv.DictWriter(test_file, fieldnames=fieldnames)

            time_str = time.strftime("%H-%M-%S")

            writer.writeheader()
            writer.writerow({'time': time_str, 'last_name': 'Beans'})

export_test_results = ExportTestResults()

export_test_results.write_to_file()
