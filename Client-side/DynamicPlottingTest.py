# Taken from http://stackoverflow.com/questions/10944621/dynamically-updating-plot-in-matplotlib

from Prediction import Prediction

import matplotlib.pyplot as plt
import time

class DynamicUpdate():
    plt.ion()

    # x range
    min_x = 0
    max_x = 10

    def on_launch(self):
        # Set up plot
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([], [])

        # Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
        self.ax.set_xlim(self.min_x, self.max_x)

        # Apply grid to graph
        self.ax.grid()

    def on_running(self, xdata, ydata):
        # Update data (with the new _and_ the old points)
        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)

        # Rescales graphs
        self.ax.relim()
        self.ax.autoscale_view()

        # Draws graph onto canvas
        self.figure.canvas.draw()

        # Clear events from canvas
        self.figure.canvas.flush_events()

    def __call__(self):
        self.on_launch()
        xdata = []
        ydata = []

        sampleData = [400, 400, 350, 500, 400, 400, 500, 500, 300, 600]

        i = 0
        while i < len(sampleData):
            xdata.append(i)
            print xdata

            ydata.append(sampleData[i])
            print ydata

            self.on_running(xdata, ydata)
            # Plot once per second
            time.sleep(1)

            i = i + 1

        prediction = Prediction()
        print prediction.Predict(xdata, ydata)

        return xdata, ydata

d = DynamicUpdate()
d()