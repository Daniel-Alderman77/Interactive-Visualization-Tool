# Based upon
# http://stackoverflow.com/questions/2745329/how-to-make-scipy-interpolate-give-an-extrapolated-result-beyond-the-input-range
import glob
import numpy as np
import os
from scipy.interpolate import InterpolatedUnivariateSpline

import FileHandler


class PredictionAlgorithm:

    def __init__(self):
        self.name = self

    # TODO - Implement Linear Regression
    # TODO - Implement Random Forest Regression
    # TODO - Implement Regression Analysis
    def predict(self, xi, yi):

        # positions to extrapolate last element in array 1 position
        x = np.linspace(0, xi[-1], 1)

        # when k = 1, linear extrapolation
        extrapolate = InterpolatedUnivariateSpline(xi, yi, k=1)
        y = extrapolate(x)

        results = [x, y]

        return results


class DataStore:

    def __init__(self):
        self.name = self

    def get_prediction_cache_file_count(self):
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

            except:
                print "File cannot be removed"

        else:
            print "Less than 4 files in prediction_cache"

            with open(os.path.join(prediction_cache_path, filename), 'wb') as data_file:
                data_file.write(data_file_contents)

    # TODO - Implement coldstart prediction
    def coldstart_prediction(self):
        client = FileHandler.WebServiceClient()

        if client.get_file_count()["Number of files"] > 0:
            print "Files are available for coldstart prediction"

        else:
            print "Files are not available for coldstart prediction"
