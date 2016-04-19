# Based upon http://stackoverflow.com/questions/2745329/how-to-make-scipy-interpolate-give-an-extrapolated-result-beyond-the-input-range

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline

class Prediction:

    def __init__(self):
        self.name = self

    def Predict(self, data):

        results = None

        return results

# given values
xi = np.array([0, 1, 2, 3, 4, 5])
yi = np.array([0.3, 0.3, -0.1, 0.2, 0.1, 0.4])

# positions to extrapolate, x = last element in array + 1
x = np.linspace(0, xi[-1] + 1, 50)

plt.figure()

# when k = 1, linear extrapolation
extrapolate = InterpolatedUnivariateSpline(xi, yi, k=1)
y = extrapolate(x)

plt.plot(x, y)
plt.show()
