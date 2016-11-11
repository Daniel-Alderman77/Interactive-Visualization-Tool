import cPickle
import random
from matplotlib import pyplot as plt
import math

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


class CPUGraph(LineGraph):

    def __init__(self):
        LineGraph.__init__(self)
        self.name = self
        self.cpu_values = []

        # First set up the figure, the axis, and the plot element we want to animate
        self.ax = plt.axes(xlim=(0, 10), ylim=(0, 500))
        self.ax.set_title('CPU Usage Over Time')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('CPU Usage')

        # Set up line animated lines to be plotted
        self.cpu, = self.ax.plot([], [], lw=2)
        self.average, = self.ax.plot([], [], lw=2)

        # Set up legend
        self.ax.legend((self.cpu, self.average), ('Current Utilisation', 'Average Utilisation'))

    # animation function.  This is called sequentially
    def animate(self, i):
        try:
            pickle_file = 'visualizer_cache/cpu_data.p'
            # Read data file from cache
            with open(pickle_file, 'rb') as pickle:
                cpu_data = cPickle.load(pickle)

            x = self.randomise_values()[0]

            cpu_value = cpu_data[0][0]['1']

            self.cpu_values.append(cpu_value)

            print("CPU value: %s" % cpu_value)

            # Animate CPU utilisation
            y = cpu_value

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.cpu.set_data(x, y)

            # Animate average cpu utilisation
            total_cpu_values = 0

            for i in self.cpu_values:
                total_cpu_values += int(i)

            y = total_cpu_values / len(self.cpu_values)

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.average.set_data(x, y)

            # Update graph
            plt.draw()

        except Exception as e:
            print(e)
            print "No CPU data available"
            pass


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
        try:
            pickle_file = 'visualizer_cache/memory_data.p'
            # Read data file from cache
            with open(pickle_file, 'rb') as pickle:
                memory_data = cPickle.load(pickle)

            memory_value = memory_data[1]['memory'][0]
            print("Memory value: %s" % memory_value)

            x = self.randomise_values()[0]
            y = memory_value

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.line.set_data(x, y)
            plt.draw()
            return self.line,

        except Exception as e:
            print(e)
            print "No memory data available"
            pass


class JobsGraph(LineGraph):

    def __init__(self):
        LineGraph.__init__(self)
        self.name = self

        # Set up the figure and the axis
        self.ax = plt.axes(xlim=(0, 10), ylim=(0, 50))
        self.ax.set_title('Number of jobs running over time')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Number of jobs running')

        # Set up line animated lines to be plotted
        self.node1, = self.ax.plot([], [], lw=2)
        self.node2, = self.ax.plot([], [], lw=2)
        self.average, = self.ax.plot([], [], lw=2)

        # Set up legend
        self.ax.legend((self.node1, self.node2, self.average), ('Node 1', 'Node 2', 'Average Number of Jobs'))

    # animation function.  This is called sequentially
    def animate(self, i):
        try:
            pickle_file = 'visualizer_cache/jobs_data.p'
            # Read data file from cache
            with open(pickle_file, 'rb') as pickle:
                jobs_data = cPickle.load(pickle)

            x = self.randomise_values()[0]

            node1_jobs = 0
            node2_jobs = 0

            for i in jobs_data[2]:
                for key in i:
                    if key == '1':
                        node1_jobs += 1
                    else:
                        node2_jobs += 1

            # Animate node 1 line
            y = node1_jobs

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.node1.set_data(x, y)

            # Animate node 2 line
            y = node2_jobs

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.node2.set_data(x, y)

            # Animate average jobs line
            average_jobs = jobs_data[1] / jobs_data[0]
            print("Average number of jobs: %s" % average_jobs)

            y = average_jobs

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.average.set_data(x, y)

            # Update graph
            plt.draw()

        except Exception as e:
            print(e)
            print "No jobs data available"
            pass


class EnergyGraph(LineGraph):

    def __init__(self):
        LineGraph.__init__(self)
        self.name = self
        self.energy_values = []

        # First set up the figure, the axis, and the plot element we want to animate
        self.ax = plt.axes(xlim=(0, 10), ylim=(0, 15000))
        self.ax.set_title('Energy Usage Over Time')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Energy Usage')

        # Set up line animated lines to be plotted
        self.energy, = self.ax.plot([], [], lw=2)
        self.average, = self.ax.plot([], [], lw=2)

        # Set up legend
        self.ax.legend((self.energy, self.average), ('Current Utilisation', 'Average Utilisation'))

    # animation function.  This is called sequentially
    def animate(self, i):
        try:
            pickle_file = 'visualizer_cache/energy_data.p'
            # Read data file from cache
            with open(pickle_file, 'rb') as pickle:
                energy_data = cPickle.load(pickle)

            x = self.randomise_values()[0]

            energy_value = energy_data[1]['energy'][0]

            self.energy_values.append(energy_value)

            print("Energy value: %s" % energy_value)

            # Animate CPU utilisation
            y = energy_value

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.energy.set_data(x, y)

            # Animate average energy usage
            total_energy_values = 0

            for i in self.energy_values:
                total_energy_values += int(i)

            y = total_energy_values / len(self.energy_values)

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.average.set_data(x, y)

            # Update graph
            plt.draw()

        except Exception as e:
            print(e)
            print "No energy data available"
            pass


class LatencyGraph(LineGraph):

    def __init__(self):
        LineGraph.__init__(self)
        self.name = self
        self.latency_values = []

        # First set up the figure, the axis, and the plot element we want to animate
        self.fig = plt.figure(figsize=(12, 5), dpi=50)
        self.ax = plt.axes(xlim=(0, 20), ylim=(0, 30))
        self.ax.set_title('Latency Over Time')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Latency')

        # Set up line animated lines to be plotted
        self.latency, = self.ax.plot([], [], lw=2)
        self.average, = self.ax.plot([], [], lw=2)

        # Set up legend
        self.ax.legend((self.latency, self.average), ('Current Latency', 'Average Latency'))

    # animation function.  This is called sequentially
    def animate(self, i):
        try:
            pickle_file = 'visualizer_cache/latency_data.p'
            # Read data file from cache
            with open(pickle_file, 'rb') as pickle:
                latency = cPickle.load(pickle)

            x = self.randomise_values()[0]

            # Convert latency from timedelta object to seconds. Then round up to the nearest second
            latency_value = math.ceil(latency.total_seconds())

            self.latency_values.append(latency_value)

            print("Current latency: %s" % latency)

            # Animate CPU utilisation
            y = latency_value

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.latency.set_data(x, y)

            # Animate average energy usage
            total_latency_values = 0

            for i in self.latency_values:
                        total_latency_values += int(i)

            y = total_latency_values / len(self.latency_values)

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.average.set_data(x, y)

            # Update graph
            plt.draw()

        except Exception as e:
            print(e)
            print "No latency data available"
            pass


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
