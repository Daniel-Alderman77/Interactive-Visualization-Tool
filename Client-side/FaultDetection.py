from ExportTestResults import ExportTestResults


class FaultDetection:

    def __init__(self):
        self.name = self

    @staticmethod
    def http_error(error):
        export_test_results = ExportTestResults()
        export_test_results.write_fault_to_file(error)

    @staticmethod
    def late_timing_fault():
        export_test_results = ExportTestResults()
        export_test_results.write_fault_to_file('Late Timing')

    @staticmethod
    def connection_error():
        export_test_results = ExportTestResults()
        export_test_results.write_fault_to_file('Connection')
