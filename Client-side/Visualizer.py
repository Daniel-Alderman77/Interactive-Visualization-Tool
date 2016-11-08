import cPickle
import random
from matplotlib import pyplot as plt

# Override the basic Tk widgets, with platform specific widgets
from tkinter.ttk import *
from Tkinter import HORIZONTAL


class LineGraph:

    def __init__(self):
        self.name = self

        # First set up the figure, the axis, and the plot element we want to animate
        self.fig = plt.figure(figsize=(7, 5), dpi=50)
        self.ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
        self.ax.set_title('Title')
        self.ax.set_xlabel('X Label')
        self.ax.set_ylabel('Y Label')
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
            self.ax.set_xlim([x[-1] - 10, x[-1]])

        self.line.set_data(x, y)
        plt.draw()
        return self.line,


# TODO - Implement CPU graph
class CPUGraph(LineGraph):

    def __init__(self):
        LineGraph.__init__(self)
        self.name = self

        # First set up the figure, the axis, and the plot element we want to animate
        self.ax = plt.axes(xlim=(0, 10), ylim=(0, 20000))
        self.ax.set_title('CPU Usage Over Time')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('CPU Usage')
        self.line, = self.ax.plot([], [], lw=2)

    # animation function.  This is called sequentially
    def animate(self, i):
        pickle_file = 'visualizer_cache/energy_data.p'
        # Read data file from cache
        with open(pickle_file, 'rb') as pickle:
            energy_data = cPickle.load(pickle)

        print("Energy value: %s" % energy_data[1]['energy'][0])

        x = self.randomise_values()[0]
        y = energy_data[1]['energy'][0]

        if x[-1] > self.ax.get_xlim()[1]:
            self.ax.set_xlim([x[-1] - 10, x[-1]])

        self.line.set_data(x, y)
        plt.draw()
        return self.line,


# TODO - Implement Memory graph
class MemoryGraph(LineGraph):

    def __init__(self):
        LineGraph.__init__(self)
        self.name = self

        # First set up the figure, the axis, and the plot element we want to animate
        self.ax = plt.axes(xlim=(0, 10), ylim=(0, 20000))
        self.ax.set_title('Memory Usage Over Time')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Memory Usage')
        self.line, = self.ax.plot([], [], lw=2)

    # animation function.  This is called sequentially
    def animate(self, i):
        pickle_file = 'visualizer_cache/energy_data.p'
        # Read data file from cache
        with open(pickle_file, 'rb') as pickle:
            energy_data = cPickle.load(pickle)

        print("Energy value: %s" % energy_data[1]['energy'][0])

        x = self.randomise_values()[0]
        y = energy_data[1]['energy'][0]

        if x[-1] > self.ax.get_xlim()[1]:
            self.ax.set_xlim([x[-1] - 10, x[-1]])

        self.line.set_data(x, y)
        plt.draw()
        return self.line,


# TODO - Implement Jobs graph
class JobsGraph(LineGraph):

    def __init__(self):
        LineGraph.__init__(self)
        self.name = self

        # First set up the figure, the axis, and the plot element we want to animate
        self.ax = plt.axes(xlim=(0, 10), ylim=(0, 20000))
        self.ax.set_title('Number of jobs running over time')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Number of jobs runnning')
        self.line, = self.ax.plot([], [], lw=2)

    # animation function.  This is called sequentially
    def animate(self, i):
        pickle_file = 'visualizer_cache/energy_data.p'
        # Read data file from cache
        with open(pickle_file, 'rb') as pickle:
            energy_data = cPickle.load(pickle)

        print("Energy value: %s" % energy_data[1]['energy'][0])

        x = self.randomise_values()[0]
        y = energy_data[1]['energy'][0]

        if x[-1] > self.ax.get_xlim()[1]:
            self.ax.set_xlim([x[-1] - 10, x[-1]])

        self.line.set_data(x, y)
        plt.draw()
        return self.line,


# TODO - Implement Energy graph
class EnergyGraph(LineGraph):

    def __init__(self):
        LineGraph.__init__(self)
        self.name = self

        # First set up the figure, the axis, and the plot element we want to animate
        self.ax = plt.axes(xlim=(0, 10), ylim=(0, 20000))
        self.ax.set_title('Energy Usage Over Time')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Energy Usage')
        self.line, = self.ax.plot([], [], lw=2)

    # animation function.  This is called sequentially
    def animate(self, i):
        pickle_file = 'visualizer_cache/energy_data.p'
        # Read data file from cache
        with open(pickle_file, 'rb') as pickle:
            energy_data = cPickle.load(pickle)

        print("Energy value: %s" % energy_data[1]['energy'][0])

        x = self.randomise_values()[0]
        y = energy_data[1]['energy'][0]

        if x[-1] > self.ax.get_xlim()[1]:
            self.ax.set_xlim([x[-1] - 10, x[-1]])

        self.line.set_data(x, y)
        plt.draw()
        return self.line,


# TODO - Implement Latency graph
class LatencyGraph(LineGraph):

    def __init__(self):
        LineGraph.__init__(self)
        self.name = self

        # First set up the figure, the axis, and the plot element we want to animate
        self.fig = plt.figure(figsize=(12, 5), dpi=50)
        self.ax = plt.axes(xlim=(0, 20), ylim=(0, 10))
        self.ax.set_title('Latency Over Time')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Latency')
        self.line, = self.ax.plot([], [], lw=2)

    # animation function.  This is called sequentially
    def animate(self, i):
        x = self.randomise_values()[0]
        y = self.randomise_values()[1]

        if x[-1] > self.ax.get_xlim()[1]:
            self.ax.set_xlim([x[-1] - 20, x[-1]])

        self.line.set_data(x, y)
        plt.draw()
        return self.line,


# TODO - Implement Gauge plot
class GaugePlot:

    def __init__(self):
        self.name = self


# TODO - Implement ProgressBar
class ProgressBar:

    def __init__(self):
        self.name = self
        self.frame = Frame()

    def draw_frame(self, progress_value):

        progress_string = "Progress through simulation - " + str(progress_value) + "%"

        progress_label = Label(self.frame, text=progress_string)
        progress_label.pack()

        progress_bar = Progressbar(self.frame, orient=HORIZONTAL, length=600, mode='determinate')
        progress_bar.pack()
        progress_bar["maximum"] = 100
        progress_bar["value"] = progress_value

        self.frame.pack()
