from ReadData import ReadData
import matplotlib.pyplot as plt

readData = ReadData()
memoryData = readData.ParseXML('Client-side/data.xml')

totalMemory = int(memoryData[0])
task1 = int(memoryData[1])
task2 = int(memoryData[2])

def MemoryAllocation(currentValue):
    # Memory Allocation
    plt.subplot(221)
    plt.plot(currentValue)
    plt.axis([0, 6, 0, 1000])
    plt.ylabel('Memory Allocation')
    plt.xlabel('Time')
    plt.title('Memory Allocation Over Time')

def Task1(currentValue):
    # Task 1
    plt.subplot(222)
    plt.plot(currentValue)
    plt.axis([0, 6, 0, 1000])
    plt.ylabel('Memory Allocation')
    plt.xlabel('Time')
    plt.title('Task 1 Memory Usage')

def Task2(currentValue):
    # Task 2
    plt.subplot(223)
    plt.plot(currentValue)
    plt.axis()
    plt.ylabel('Memory Allocation')
    plt.xlabel('Time')
    plt.title('Task 2 Memory Usage')

def Render():
    # plot with various axes scales
    plt.figure(1)

    task1Usage = [task1, 400, 350, 500, 400]
    task2Usage = [task2, 350, 400, 500, 600]

    plt.ion()
    plt.show()

    for i in range(100):


        memoryAllocation = task1Usage + task2Usage

        MemoryAllocation(memoryAllocation)
        Task1(task1Usage)
        Task2(task2Usage)

        plt.draw()
        plt.pause(0.05)

Render()