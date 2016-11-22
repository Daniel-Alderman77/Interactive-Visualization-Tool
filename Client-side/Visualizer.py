import cPickle
import random
from matplotlib import pyplot as plt
import math

# Override the basic Tk widgets, with platform specific widgets
from tkinter.ttk import *
from Tkinter import HORIZONTAL

from Prediction import PredictionAlgorithm, DataStore
from ExportTestResults import ExportTestResults
from FaultDetection import FaultDetection


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

        # Class instances
        self.export_test_results = ExportTestResults()
        self.prediction_algorithm = PredictionAlgorithm()
        self.data_store = DataStore()
        self.fault_detection = FaultDetection()

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

        # First set up the figure, the axis, and the plot element we want to animate
        self.ax = plt.axes(xlim=(0, 10), ylim=(0, 500))
        self.ax.set_title('CPU Usage Over Time')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('CPU Usage')

        # Set up line animated lines to be plotted
        self.cpu, = self.ax.plot([], [], lw=2)
        self.average, = self.ax.plot([], [], lw=2)

        # Initialise list to store plotted values for prediction
        self.prediction_index = 0
        self.x_array = []
        self.y_array = []
        
        # Set up legend
        self.ax.legend((self.cpu, self.average), ('Current Utilisation', 'Average Utilisation'))

    # animation function.  This is called sequentially
    def animate(self, i):
        try:
            pickle_file = 'visualizer_cache/cpu_data.p'
            # Read data file from cache
            with open(pickle_file, 'rb') as pickle:
                cpu_data = cPickle.load(pickle)

            cpu_value = cpu_data[0][0]['1']

            if len(self.x_array) == 0:
                self.x_array.append(0)
            else:
                x = self.x_array[-1] + 1
                self.x_array.append(x)

            self.y_array.append(cpu_value)

            print("CPU value: %s" % cpu_value)

            # # Animate cpu utilisation
            x = self.x_array
            y = self.y_array

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.cpu.set_data(x, y)

            # Animate average cpu utilisation
            total_cpu_values = 0

            for i in self.y_array:
                total_cpu_values += float(i)

            y = total_cpu_values / len(self.y_array)

            print("Average CPU value: %s" % y)

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.average.set_data(x, y)

            # Update graph
            plt.draw()

            return self.cpu, self.average,

        except Exception:
            self.fault_detection.null_values_fault('CPU')

            # If no data has previously been plotted use cold start prediction
            if self.y_array[0] == 0:

                print "Now Predicting next CPU value using cold start prediction"

                cpu_value = 0

                while cpu_value == 0:
                    self.data_store.cold_start_prediction('CPU', self.prediction_index)

                    pickle_file = 'visualizer_cache/cpu_data.p'

                    # Read data file from cache
                    with open(pickle_file, 'rb') as pickle:
                        cpu_data = cPickle.load(pickle)

                    cpu_value = cpu_data[0]

                    # Increment index
                    self.prediction_index += 1

                # Remove null value
                self.y_array.pop(0)

                # Append value so it can be plotted
                self.y_array.append(cpu_value)

                print("Cold start prediction has prediction %s as the next CPU value" % cpu_value)

                # Reset prediction cache index back to zero
                self.prediction_index = 0

                self.export_test_results.write_predicted_value_to_file(cpu_value, 'CPU')

                try:
                    # Animate cpu utilisation
                    x = self.x_array

                    y = self.y_array

                    if x[-1] > self.ax.get_xlim()[1]:
                        self.ax.set_xlim([x[-1] - 10, x[-1]])

                    self.cpu.set_data(x, y)

                    # Animate average cpu utilisation
                    total_cpu_values = 0

                    for i in self.y_array:
                        total_cpu_values += float(i)

                    y = total_cpu_values / len(self.y_array)

                    print("Average CPU value: %s" % y)

                    if x[-1] > self.ax.get_xlim()[1]:
                        self.ax.set_xlim([x[-1] - 10, x[-1]])

                    self.average.set_data(x, y)

                    # Update graph
                    plt.draw()

                    return self.cpu, self.average,

                except:
                    pass

            # Else use simple linear regression utilising previously plotted data
            else:
                print "Now Predicting next CPU value using simple linear regression"

                try:
                    n = len(self.y_array) - 1

                    y = self.y_array[0]

                    if n == 1:
                        self.y_array[1] = y

                    else:
                        del self.x_array[-1]
                        del self.y_array[-1]

                        y = self.prediction_algorithm.simple_linear_regression(self.x_array, self.y_array, n)

                        self.x_array.append(n)
                        self.y_array.append(y)

                        print("Simple linear regression has prediction %s as the next CPU value" % y)

                    # Animate cpu utilisation
                    x = self.x_array
                    y = self.y_array

                    if x[-1] > self.ax.get_xlim()[1]:
                        self.ax.set_xlim([x[-1] - 10, x[-1]])

                    self.cpu.set_data(x, y)

                    # Animate average cpu utilisation
                    total_cpu_values = 0

                    for i in self.y_array:
                        total_cpu_values += float(i)

                    y = total_cpu_values / len(self.y_array)

                    print("Average CPU value: %s" % y)

                    if x[-1] > self.ax.get_xlim()[1]:
                        self.ax.set_xlim([x[-1] - 10, x[-1]])

                    self.average.set_data(x, y)

                    # Update graph
                    plt.draw()

                    # Write to test file

                    self.export_test_results.write_predicted_value_to_file(y, 'CPU')

                    return self.cpu, self.average,

                except:
                    pass


class MemoryGraph(LineGraph):

    def __init__(self):
        LineGraph.__init__(self)
        self.name = self

        # First set up the figure, the axis, and the plot element we want to animate
        self.ax = plt.axes(xlim=(0, 10), ylim=(0, 25000))
        self.ax.set_title('Memory Usage Over Time')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Memory Usage')
        self.memory, = self.ax.plot([], [], lw=2)
        self.average, = self.ax.plot([], [], lw=2)

        # Initialise list to store plotted values for prediction
        self.prediction_index = 0
        self.x_array = []
        self.y_array = []

        # Set up legend
        self.ax.legend((self.memory, self.average), ('Current Utilisation', 'Average Utilisation'))

    # animation function.  This is called sequentially
    def animate(self, i):
        try:
            pickle_file = 'visualizer_cache/memory_data.p'
            # Read data file from cache
            with open(pickle_file, 'rb') as pickle:
                memory_data = cPickle.load(pickle)

            memory_value = memory_data[0]

            if len(self.x_array) == 0:
                self.x_array.append(0)
            else:
                x = self.x_array[-1] + 1
                self.x_array.append(x)

            self.y_array.append(memory_value)

            print("Memory value: %s" % memory_value)

            # if memory_value == 0 throw exception
            assert memory_value != 0

            # Animate cpu utilisation
            x = self.x_array
            y = self.y_array

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.memory.set_data(x, y)

            # Animate average cpu utilisation
            total_memory_values = 0

            for i in self.y_array:
                total_memory_values += float(i)

            y = total_memory_values / len(self.y_array)

            print("Average Memory value: %s" % y)

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.average.set_data(x, y)

            # Update graph
            plt.draw()

            return self.memory, self.average,

        except Exception:
            self.fault_detection.null_values_fault('Memory')

            # If no data has previously been plotted use cold start prediction
            if self.y_array[0] == 0:
                print "Now Predicting next Memory value using cold start prediction"

                memory_value = 0

                while memory_value == 0:
                    self.data_store.cold_start_prediction('Memory', self.prediction_index)

                    pickle_file = 'visualizer_cache/memory_data.p'
                    # Read data file from cache
                    with open(pickle_file, 'rb') as pickle:
                        memory_data = cPickle.load(pickle)

                    memory_value = memory_data[0]

                    # Increment index
                    self.prediction_index += 1

                # Remove null value
                self.y_array.pop(0)
                
                # Append value so it can be plotted
                self.y_array.append(memory_value)

                print("Cold start prediction has prediction %s as the next Memory value" % memory_value)

                # Reset prediction cache index back to zero
                self.prediction_index = 0

                self.export_test_results.write_predicted_value_to_file(memory_value, 'Memory')

                try:
                    # Animate cpu utilisation
                    x = self.x_array
                    y = self.y_array

                    if x[-1] > self.ax.get_xlim()[1]:
                        self.ax.set_xlim([x[-1] - 10, x[-1]])

                    self.memory.set_data(x, y)

                    # Animate average cpu utilisation
                    total_memory_values = 0

                    for i in self.y_array:
                        total_memory_values += float(i)

                    y = total_memory_values / len(self.y_array)

                    print("Average Memory value: %s" % y)

                    if x[-1] > self.ax.get_xlim()[1]:
                        self.ax.set_xlim([x[-1] - 10, x[-1]])

                    self.average.set_data(x, y)

                    # Update graph
                    plt.draw()

                    return self.memory, self.average,

                except:
                    pass

            # Else use simple linear regression utilising previously plotted data
            else:
                print "Now Predicting next Memory value using simple linear regression"

                try:
                    n = len(self.y_array) - 1
                    y = self.y_array[0]

                    if n == 1:
                        self.y_array[1] = y
                    else:
                        del self.x_array[-1]
                        del self.y_array[-1]

                        y = self.prediction_algorithm.simple_linear_regression(self.x_array, self.y_array, n)

                        self.x_array.append(n)
                        self.y_array.append(y)

                        print("Simple linear regression has prediction %s as the next Memory value" % y)

                    # Animate cpu utilisation
                    x = self.x_array
                    y = self.y_array

                    if x[-1] > self.ax.get_xlim()[1]:
                        self.ax.set_xlim([x[-1] - 10, x[-1]])

                    self.memory.set_data(x, y)

                    # Animate average cpu utilisation
                    total_memory_values = 0

                    for i in self.y_array:
                        total_memory_values += float(i)

                    y = total_memory_values / len(self.y_array)

                    print("Average Memory value: %s" % y)

                    if x[-1] > self.ax.get_xlim()[1]:
                        self.ax.set_xlim([x[-1] - 10, x[-1]])

                    self.average.set_data(x, y)

                    # Update graph
                    plt.draw()

                    # Write to test file
                    self.export_test_results.write_predicted_value_to_file(y, 'Memory')

                    return self.memory, self.average,

                except:
                    pass


class JobsGraph(LineGraph):

    def __init__(self):
        LineGraph.__init__(self)
        self.name = self

        # Set up the figure and the axis
        self.ax = plt.axes(xlim=(0, 10), ylim=(0, 100))
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

        except Exception:
            print "Now Predicting next Jobs value"
            # TODO - Predict next value
            pass


class EnergyGraph(LineGraph):

    def __init__(self):
        LineGraph.__init__(self)
        self.name = self

        # First set up the figure, the axis, and the plot element we want to animate
        self.ax = plt.axes(xlim=(0, 10), ylim=(0, 20000))
        self.ax.set_title('Energy Usage Over Time')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Energy Usage')

        # Set up line animated lines to be plotted
        self.energy, = self.ax.plot([], [], lw=2)
        self.average, = self.ax.plot([], [], lw=2)

        # Initialise list to store plotted values for prediction
        self.prediction_index = 0
        self.x_array = []
        self.y_array = []

        # Set up legend
        self.ax.legend((self.energy, self.average), ('Current Utilisation', 'Average Utilisation'))

    # animation function.  This is called sequentially
    def animate(self, i):
        try:
            pickle_file = 'visualizer_cache/energy_data.p'
            # Read data file from cache
            with open(pickle_file, 'rb') as pickle:
                energy_data = cPickle.load(pickle)

            energy_value = energy_data[1]['energy'][0]

            if len(self.x_array) == 0:
                self.x_array.append(0)
            else:
                x = self.x_array[-1] + 1
                self.x_array.append(x)

            self.y_array.append(energy_value)

            print("Energy value: %s" % energy_value)

            # Animate cpu utilisation
            x = self.x_array
            y = self.y_array

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.energy.set_data(x, y)

            # Animate average energy usage
            total_energy_values = 0

            for i in self.y_array:
                total_energy_values += float(i)

            y = total_energy_values / len(self.y_array)

            print("Average CPU value: %s" % y)

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.average.set_data(x, y)

            # Update graph
            plt.draw()

            return self.energy, self.average,

        except Exception:
            self.fault_detection.null_values_fault('Energy')

            # If no data has previously been plotted use cold start prediction
            if self.y_array[0] == 0:

                print "Now Predicting next Energy value using cold start prediction"

                energy_value = 0

                while energy_value == 0:
                    self.data_store.cold_start_prediction('Energy', self.prediction_index)

                    pickle_file = 'visualizer_cache/energy_data.p'

                    # Read data file from cache
                    with open(pickle_file, 'rb') as pickle:
                        memory_data = cPickle.load(pickle)

                    energy_value = memory_data[0]

                    # Increment index
                    self.prediction_index += 1

                # Remove null value
                self.y_array.pop(0)

                # Append value so it can be plotted
                self.y_array.append(energy_value)

                print("Cold start prediction has prediction %s as the next Energy value" % energy_value)

                # Reset prediction cache index back to zero
                self.prediction_index = 0

                try:
                    # Animate cpu utilisation
                    x = self.x_array
                    y = self.y_array

                    if x[-1] > self.ax.get_xlim()[1]:
                        self.ax.set_xlim([x[-1] - 10, x[-1]])

                    self.energy.set_data(x, y)

                    # Animate average cpu utilisation
                    total_energy_values = 0

                    for i in self.y_array:
                        total_energy_values += float(i)

                    y = total_energy_values / len(self.y_array)

                    print("Average Energy value: %s" % y)

                    if x[-1] > self.ax.get_xlim()[1]:
                        self.ax.set_xlim([x[-1] - 10, x[-1]])

                    self.average.set_data(x, y)

                    # Update graph
                    plt.draw()

                    return self.energy, self.average,

                except:
                    pass

            # Else use simple linear regression utilising previously plotted data
            else:
                print "Now Predicting next Energy value using simple linear regression"

                try:
                    n = len(self.y_array) - 1

                    y = self.y_array[0]

                    if n == 1:
                        self.y_array[1] = y

                    else:
                        del self.x_array[-1]
                        del self.y_array[-1]

                        y = self.prediction_algorithm.simple_linear_regression(self.x_array, self.y_array, n)

                        self.x_array.append(n)
                        self.y_array.append(y)

                        print("Simple linear regression has prediction %s as the next Energy value" % y)

                    # Animate cpu utilisation
                    x = self.x_array
                    y = self.y_array

                    if x[-1] > self.ax.get_xlim()[1]:
                        self.ax.set_xlim([x[-1] - 10, x[-1]])

                    self.energy.set_data(x, y)

                    # Animate average cpu utilisation
                    total_energy_values = 0

                    for i in self.y_array:
                        total_energy_values += float(i)

                    y = total_energy_values / len(self.y_array)

                    print("Average Energy value: %s" % y)

                    if x[-1] > self.ax.get_xlim()[1]:
                        self.ax.set_xlim([x[-1] - 10, x[-1]])

                    self.average.set_data(x, y)

                    # Update graph
                    plt.draw()

                    # Write to test file
                    self.export_test_results.write_predicted_value_to_file(y, 'Energy')

                    return self.energy, self.average,

                except:
                    pass


class LatencyGraph(LineGraph):

    def __init__(self):
        LineGraph.__init__(self)
        self.name = self

        # First set up the figure, the axis, and the plot element we want to animate
        self.fig = plt.figure(figsize=(12, 5), dpi=50)
        self.ax = plt.axes(xlim=(0, 20), ylim=(0, 2))
        self.ax.set_title('Latency Over Time')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Latency (seconds)')

        # Set up line animated lines to be plotted
        self.latency, = self.ax.plot([], [], lw=2)
        self.average, = self.ax.plot([], [], lw=2)

        # Initialise list to store plotted values for prediction
        self.prediction_index = 0
        self.x_array = []
        self.y_array = []

        # Set up legend
        self.ax.legend((self.latency, self.average), ('Current Latency', 'Average Latency'))

    # animation function.  This is called sequentially
    def animate(self, i):
        try:
            pickle_file = 'visualizer_cache/latency_data.p'
            # Read data file from cache
            with open(pickle_file, 'rb') as pickle:
                latency = cPickle.load(pickle)

            if len(self.x_array) == 0:
                self.x_array.append(0)
            else:
                x = self.x_array[-1] + 1
                self.x_array.append(x)

            # Convert latency from timedelta object to seconds. Then round up to the nearest second
            latency_value = math.ceil(latency.total_seconds())

            self.y_array.append(latency_value)

            print("Current latency: %s" % latency)

            # Animate current latency
            x = self.x_array
            y = self.y_array

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.latency.set_data(x, y)

            # Animate average latency
            total_latency_values = 0

            for i in self.y_array:
                total_latency_values += int(i)

            y = total_latency_values / len(self.y_array)

            print("Average Latency value: %s" % y)

            if x[-1] > self.ax.get_xlim()[1]:
                self.ax.set_xlim([x[-1] - 10, x[-1]])

            self.average.set_data(x, y)

            # Update graph
            plt.draw()

            return self.latency, self.average,

        except Exception:
            self.fault_detection.null_values_fault('Energy')

            # If no data has previously been plotted use cold start prediction
            if self.y_array[0] == 0:
                print "Now Predicting next Latency value using cold start prediction"

                energy_value = 0

                while energy_value == 0:
                    self.data_store.cold_start_prediction('Latency', self.prediction_index)

                    pickle_file = 'visualizer_cache/latency_data.p'
                    # Read data file from cache
                    with open(pickle_file, 'rb') as pickle:
                        latency = cPickle.load(pickle)

                    energy_value = latency

                    # Increment index
                    self.prediction_index += 1

                # Remove null value
                self.y_array.pop(0)

                # Append value so it can be plotted
                self.y_array.append(energy_value)

                print("Cold start prediction has prediction %s as the next Latency value" % energy_value)

                # Reset prediction cache index back to zero
                self.prediction_index = 0

                try:
                    # Animate cpu utilisation
                    x = self.x_array
                    y = self.y_array

                    if x[-1] > self.ax.get_xlim()[1]:
                        self.ax.set_xlim([x[-1] - 10, x[-1]])

                    self.latency.set_data(x, y)

                    # Animate average cpu utilisation
                    total_latency_values = 0

                    for i in self.y_array:
                        total_latency_values += float(i)

                    y = total_latency_values / len(self.y_array)

                    print("Average Latency value: %s" % y)

                    if x[-1] > self.ax.get_xlim()[1]:
                        self.ax.set_xlim([x[-1] - 10, x[-1]])

                    self.average.set_data(x, y)

                    # Update graph
                    plt.draw()

                    return self.latency, self.average,

                except:
                    pass

            # Else use simple linear regression utilising previously plotted data
            else:
                print "Now Predicting next Latency value using simple linear regression"

                try:
                    n = len(self.y_array) - 1

                    y = self.y_array[0]

                    if n == 1:
                        self.y_array[1] = y

                    else:
                        del self.x_array[-1]
                        del self.y_array[-1]

                        y = self.prediction_algorithm.simple_linear_regression(self.x_array, self.y_array, n)

                        self.x_array.append(n)
                        self.y_array.append(y)

                        print("Simple linear regression has prediction %s as the next Latency value" % y)

                    # Animate current latency
                    x = self.x_array
                    y = self.y_array

                    if x[-1] > self.ax.get_xlim()[1]:
                        self.ax.set_xlim([x[-1] - 10, x[-1]])

                    self.latency.set_data(x, y)

                    # Animate average latency
                    total_latency_values = 0

                    for i in self.y_array:
                        total_latency_values += float(i)

                    y = total_latency_values / len(self.y_array)

                    print("Average Latency value: %s" % y)

                    if x[-1] > self.ax.get_xlim()[1]:
                        self.ax.set_xlim([x[-1] - 10, x[-1]])

                    self.average.set_data(x, y)

                    # Update graph
                    plt.draw()

                    # Write to test file
                    self.export_test_results.write_predicted_value_to_file(y, 'Latency')

                    return self.latency, self.average,

                except:
                    pass


# TODO - (Extension) Implement Gauge plot
class GaugePlot:

    def __init__(self):
        self.name = self


# TODO - (Extension) Implement ProgressBar
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
