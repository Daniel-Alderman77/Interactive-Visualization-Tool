import glob
import os
from scipy import stats

from ExportTestResults import ExportTestResults
from FileHandler import ResponseDeserialization


class PredictionAlgorithm:

    def __init__(self):
        self.name = self

    # TODO - (Extension) Implement Random Forest Regression
    # TODO - (Extension) Implement Regression Analysis

    @staticmethod
    def simple_linear_regression(x_data, y_data, x):

        # Computes least-squares regression with x and y measurements
        slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)

        # For given x compute y value
        y = intercept + (slope * x)

        return y


class DataStore:

    def __init__(self):
        self.name = self
        self.prediction_cache_path = "prediction_cache"

        # Class instances
        self.export_test_results = ExportTestResults()
        self.response_deserialization = ResponseDeserialization()

    def get_prediction_cache_file_count(self):
        file_count = (len(glob.glob1(self.prediction_cache_path, "*.xml")))

        list_of_files = []
        if file_count > 0:
            list_of_files = glob.glob1(self.prediction_cache_path, "*.xml")

        return file_count, list_of_files

    def prediction_cache(self, filename, data_file_contents):
        # If prediction cache doesn't exist create it
        if not os.path.exists(self.prediction_cache_path):
            os.makedirs(self.prediction_cache_path)

        # Check if number of files in cache is > 30
        if self.get_prediction_cache_file_count()[0] > 30:
            print "Greater than 30 files in prediction_cache"

            try:
                # Remove oldest file in prediction cache
                oldest_file = self.get_prediction_cache_file_count()[1][0]

                os.remove(self.prediction_cache_path + "/" + oldest_file)

                print "Oldest file " + oldest_file + " removed"

                # Write new file as replacement
                with open(os.path.join(self.prediction_cache_path, filename), 'wb') as data_file:
                    data_file.write(data_file_contents)

                print "New file " + filename + " written as replacement"

            except Exception as e:
                print(e)
                print "File cannot be removed"
                pass

        else:
            print "Less than 30 files in prediction_cache"

            # Write file to prediction cache
            with open(os.path.join(self.prediction_cache_path, filename), 'wb') as data_file:
                data_file.write(data_file_contents)

            print "Wrote " + filename + " to prediction cache"

    def cold_start_prediction(self, type_of_data, index):

        if self.get_prediction_cache_file_count > 0:
            print "Files are available for cold start prediction"

            try:
                filename = self.get_prediction_cache_file_count()[1][index]

                # Pass file prediction cache to File Handler to be deserialized
                if type_of_data == 'CPU':
                    self.response_deserialization.parse_cpu_data('prediction_cache/' + filename)
                if type_of_data == 'Memory':
                    self.response_deserialization.parse_memory_data('prediction_cache/' + filename)
                if type_of_data == 'Jobs':
                    self.response_deserialization.parse_jobs_data('prediction_cache/' + filename)
                if type_of_data == 'Energy':
                    self.response_deserialization.parse_energy_data('prediction_cache/' + filename)

            except IndexError:
                print 'Cold start prediction has exhausted files in prediction cache for ' + type_of_data

                self.export_test_results.write_fault_to_file('Exhausted files in prediction cache')

        else:
            print "No files are available for cold start prediction"

            self.export_test_results.write_fault_to_file('No files are available for cold start prediction')
