import glob
import os
from scipy import stats


class PredictionAlgorithm:

    def __init__(self):
        self.name = self

    # TODO - Implement Linear Regression
    # TODO - (Extension) Implement Random Forest Regression
    # TODO - (Extension) Implement Regression Analysis

    @staticmethod
    def simple_linear_regression(x_data, y_data, x):

        # Computes least-squares regression with x and y measurements
        slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)

        # For given x compute y value
        y = intercept + (slope * x)

        return y

prediction_algorithm = PredictionAlgorithm()

xi = [17, 13, 12, 15, 16, 14, 16, 16, 18, 19]
yi = [94, 73, 59, 80, 93, 85, 66, 79, 77, 91]

prediction_algorithm.simple_linear_regression(xi, yi, 15)


class DataStore:

    def __init__(self):
        self.name = self

    @staticmethod
    def get_prediction_cache_file_count():
        file_count = (len(glob.glob1("data_store", "*.xml")))

        list_of_files = []
        if file_count > 0:
            list_of_files = glob.glob1("data_store", "*.xml")

        return file_count, list_of_files

    def prediction_cache(self, filename, data_file_contents):

        prediction_cache_path = "prediction_cache"

        if not os.path.exists(prediction_cache_path):
            os.makedirs(prediction_cache_path)

        # Check if number of files in cache is > 4
        if self.get_prediction_cache_file_count()[0] > 4:
            print "Greater than 4 files in prediction_cache"

            try:
                # Remove oldest file in prediction cache
                oldest_file = self.get_prediction_cache_file_count()[1][0]

                os.remove(prediction_cache_path + oldest_file)

                print "Oldest file " + oldest_file + " removed"

                # Write new file as replacement
                with open(os.path.join(prediction_cache_path, filename), 'wb') as data_file:
                    data_file.write(data_file_contents)

                print "New file " + filename + " written as replacement"

            except Exception as e:
                print(e)
                print "File cannot be removed"
                pass

        else:
            print "Less than 4 files in prediction_cache"

            with open(os.path.join(prediction_cache_path, filename), 'wb') as data_file:
                data_file.write(data_file_contents)

    # TODO - Implement cold start prediction
    # @staticmethod
    # def cold_start_prediction():
    #     client = FileHandler.WebServiceClient()
    #
    #     if client.get_local_file_count()["Number of files"] > 0:
    #         print "Files are available for cold start prediction"
    #
    #     else:
    #         print "Files are not available for cold start prediction"
