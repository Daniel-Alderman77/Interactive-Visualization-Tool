from ReadData import ReadData
import matplotlib.pyplot as plt

readData = ReadData()
memoryData = readData.ParseXML('data.xml')

totalMemory = int(memoryData[0])
task1 = int(memoryData[1])
task2 = int(memoryData[2])

def Render():
    # plot with various axes scales
    plt.figure(1)

    # Memory Allocation
    plt.subplot(221)
    plt.plot([task1 + task2, 700, 600, 500, 800])
    plt.axis([0, 6, 0, 1000])
    plt.ylabel('Memory Allocation')
    plt.xlabel('Time')
    plt.title('Memory Allocation Over Time')

    # Task 1
    plt.subplot(222)
    plt.plot(totalMemory - (task1 + task2))
    plt.axis([0, 6, 0, 1000])
    plt.ylabel('Memory Allocation')
    plt.xlabel('Time')
    plt.title('Task 1 Memory Usage')

    # Task 2
    plt.subplot(223)
    plt.plot(totalMemory - (task1 + task2))
    plt.axis([0, 6, 0, 1000])
    plt.ylabel('Memory Allocation')
    plt.xlabel('Time')
    plt.title('Task 2 Memory Usage')

    plt.show()

Render()