from ExportTestResults import ExportTestResults


class FaultDetection:

    def __init__(self):
        self.name = self

    # TODO - Implement Late-timing fault detection

    @staticmethod
    def http_404():
        export_test_results = ExportTestResults()
        export_test_results.write_fault_to_file('HTTP 404')

    # TODO - Implement 500 internal server error fault detection
