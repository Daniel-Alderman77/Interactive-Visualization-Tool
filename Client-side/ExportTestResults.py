import csv

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
        with open('test_results/test.csv', 'wb') as test_file:
            fieldnames = ['first_name', 'last_name']
            writer = csv.DictWriter(test_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
            writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
            writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

export_test_results = ExportTestResults()

export_test_results.write_to_file()
