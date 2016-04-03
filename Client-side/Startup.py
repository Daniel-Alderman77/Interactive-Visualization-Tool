from ReadData import ReadData
from RestClient import RestClient

import matplotlib.pyplot as plt

class Startup():

    def __init__(self):
        self.name = self

    def MemoryAllocation(self, currentValue):
        plt.subplot(221)
        plt.plot(currentValue)
        plt.axis([0, 6, 0, 1000])
        plt.ylabel('Memory Allocation')
        plt.xlabel('Time')
        plt.title('Memory Allocation Over Time')

    def Task1(self, currentValue):
        plt.subplot(222)
        plt.plot(currentValue)
        plt.axis([0, 6, 0, 1000])
        plt.ylabel('Memory Allocation')
        plt.xlabel('Time')
        plt.title('Task 1 Memory Usage')

    def Task2(self, currentValue):
        plt.subplot(223)
        plt.plot(currentValue)
        plt.axis()
        plt.ylabel('Memory Allocation')
        plt.xlabel('Time')
        plt.title('Task 2 Memory Usage')

    def __call__(self):

        readData = ReadData()
        memoryData = readData.ParseXML('Client-side/data.xml')

        restClient = RestClient()
        restClient.GetRequest()

        totalMemory = int(memoryData[0])
        task1 = int(memoryData[1])
        task2 = int(memoryData[2])

        # plot with various axes scales
        plt.figure(1)

        task1Usage = [task1, 400, 350, 500, 400]
        task2Usage = [task2, 350, 400, 500, 600]

        plt.ion()
        plt.show()

        # Number of times the animation refreshes
        for i in range(10):

            memoryAllocation = task1Usage + task2Usage

            self.MemoryAllocation(memoryAllocation)
            self.Task1(task1Usage)
            self.Task2(task2Usage)

            plt.draw()
            plt.pause(0.05)

startup = Startup()
startup()