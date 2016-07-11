from FileHandler import ResponseDeserialization
from RESTClient import RESTClient

import matplotlib.pyplot as plt


class Startup:

    def __init__(self):
        self.name = self

    def memory_allocation(self, current_value):
        plt.subplot(221)
        plt.plot(current_value)
        plt.axis([0, 6, 0, 1000])
        plt.ylabel('Memory Allocation')
        plt.xlabel('Time')
        plt.title('Memory Allocation Over Time')

    def task1(self, current_value):
        plt.subplot(222)
        plt.plot(current_value)
        plt.axis([0, 6, 0, 1000])
        plt.ylabel('Memory Allocation')
        plt.xlabel('Time')
        plt.title('Task 1 Memory Usage')

    def task2(self, current_value):
        plt.subplot(223)
        plt.plot(current_value)
        plt.axis()
        plt.ylabel('Memory Allocation')
        plt.xlabel('Time')
        plt.title('Task 2 Memory Usage')

    def __call__(self):

        read_data = ResponseDeserialization()
        memory_data = read_data.parse_memory_data('data_store/data.xml')

        rest_client = RESTClient()
        rest_client()

        total_memory = int(memory_data[0])
        task1 = int(memory_data[1])
        task2 = int(memory_data[2])

        # plot with various axes scales
        plt.figure(1)

        task1_usage = [task1, 400, 350, 500, 400]
        task2_usage = [task2, 350, 400, 500, 600]

        plt.ion()
        plt.show()

        # Number of times the animation refreshes
        for i in range(10):

            memory_allocation = task1_usage + task2_usage

            self.memory_allocation(memory_allocation)
            self.task1(task1_usage)
            self.task2(task2_usage)

            plt.draw()
            plt.pause(0.05)

startup = Startup()
startup()
