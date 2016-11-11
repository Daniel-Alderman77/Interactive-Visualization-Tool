from ExportTestResults import ExportTestResults


class FaultDetection:

    def __init__(self):
        self.name = self

    # TODO - Implement Late-timing fault detection

    # TODO - Implement 404 resource not found fault detection
    @staticmethod
    def http_404():
        export_test_results = ExportTestResults()
        export_test_results.write_fault_to_file('404')
