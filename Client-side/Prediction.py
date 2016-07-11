# Based upon
# http://stackoverflow.com/questions/2745329/how-to-make-scipy-interpolate-give-an-extrapolated-result-beyond-the-input-range

import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline


class PredictionAlgorithm:

    def __init__(self):
        self.name = self

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
