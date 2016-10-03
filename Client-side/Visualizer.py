import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from numpy import arange, sin, pi

import random

from matplotlib import pyplot as plt

from FileHandler import ResponseDeserialization

# TODO - Implement Visualizer
# TODO - Implement line graphs
# TODO - Implement Guage plot
# TODO - Implement real-time plotting


class Visualizer:

    def __init__(self):
        self.name = self

    # TODO - Implement CPU graph
    # TODO - Implement Memory graph
    # TODO - Implement Jobs graph

    # TODO - Implement energy graph
    def draw_energy_graph(self, frame, row, column):
        response_deserialization = ResponseDeserialization()

        print response_deserialization.get_energy_visualizer_data()

        figure = Figure(figsize=(6, 5), dpi=60)
        subplot = figure.add_subplot(111)
        values = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * values)

        subplot.set_title('Tk embedding')
        subplot.set_xlabel('X axis label')
        subplot.set_ylabel('Y label')
        subplot.plot(values, s)

        # a tk.DrawingArea
        canvas = FigureCanvasTkAgg(figure, frame)
        canvas.show()
        canvas.get_tk_widget().grid(row=row, column=column)

    # TODO - Implement Latency graph


class LineGraph:

    def __init__(self):
        self.name = self

        # First set up the figure, the axis, and the plot element we want to animate
        self.fig = plt.figure(figsize=(6, 5), dpi=60)
        self.ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
        self.line, = self.ax.plot([], [], lw=2)

        self.x_array = []
        self.y_array = []

    # initialization function: plot the background of each frame
    def init(self):
        self.line.set_data([], [])
        return self.line,

    def randomise_values(self):
        y = random.randint(1, 9)

        if len(self.x_array) == 0:
            self.x_array.append(0)
        else:
            x = self.x_array[-1] + 1
            self.x_array.append(x)

        self.y_array.append(y)

        return self.x_array, self.y_array

    # animation function.  This is called sequentially
    def animate(self, i):
        x = self.randomise_values()[0]
        y = self.randomise_values()[1]

        if x[-1] > self.ax.get_xlim()[1]:
            self.ax.set_xlim([x[-1]-10, x[-1]])

        self.line.set_data(x, y)
        plt.draw()
        return self.line,
