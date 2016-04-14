import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QGroupBox, QFont, QLabel, QVBoxLayout, QHBoxLayout, QMainWindow
import matplotlib

matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4'] = 'PySide'
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class MainWindow():
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

    @staticmethod
    def cpu_figure():
        # Generate the plot
        fig = Figure(figsize=(4, 3), dpi=72, facecolor=(1, 1, 1), edgecolor=(0, 0, 0))
        ax = fig.add_subplot(111)
        ax.plot([0, 1])
        # Generate the canvas to display the plot
        canvas = FigureCanvas(fig)

        win = QMainWindow()
        # Add the plot canvas to a window
        win.setCentralWidget(canvas)
        return win

    def __call__(self):
        app = QApplication(sys.argv)

        # Create a QGroupBox component to act as the window

        window = QGroupBox()
        window.setWindowTitle("Main Window")

        # Create and configure widgets

        cpuLabel = QLabel()
        cpuLabel.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
        cpuLabel.setAlignment(Qt.AlignCenter)
        cpuLabel.setText("CPU Utilisation")

        memoryLabel = QLabel()
        memoryLabel.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
        memoryLabel.setAlignment(Qt.AlignCenter)
        memoryLabel.setText("Memory Utilisation")

        jobsLabel = QLabel()
        jobsLabel.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
        jobsLabel.setAlignment(Qt.AlignCenter)
        jobsLabel.setText("Current Jobs")

        hierarchyLabel = QLabel()
        hierarchyLabel.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
        hierarchyLabel.setAlignment(Qt.AlignCenter)
        hierarchyLabel.setText("Hierarchy View")

        latencyLabel = QLabel()
        latencyLabel.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
        latencyLabel.setAlignment(Qt.AlignCenter)
        latencyLabel.setText("Latency")

        # Top Layout

        topLayout = QHBoxLayout()

        topLeftLayout = QVBoxLayout()
        topLeftLayout.addWidget(cpuLabel)
        topLeftLayout.addWidget(self.cpu_figure())

        topRightLayout = QVBoxLayout()
        topRightLayout.addWidget(memoryLabel)
        topRightLayout.addWidget(self.cpu_figure())

        topLayout.addLayout(topLeftLayout)
        topLayout.addLayout(topRightLayout)

        # Middle Layout

        middleLayout = QHBoxLayout()

        middleLeftLayout = QVBoxLayout()
        middleLeftLayout.addWidget(jobsLabel)
        middleLeftLayout.addWidget(self.cpu_figure())

        middleRightLayout = QVBoxLayout()
        middleRightLayout.addWidget(hierarchyLabel)
        middleRightLayout.addWidget(self.cpu_figure())

        middleLayout.addLayout(middleLeftLayout)
        middleLayout.addLayout(middleRightLayout)

        # Bottom layout

        bottomLayout = QVBoxLayout()
        bottomLayout.addWidget(latencyLabel)
        bottomLayout.addWidget(self.cpu_figure())

        # Stack layouts on top of each other

        windowLayout = QVBoxLayout()
        windowLayout.addLayout(topLayout)
        windowLayout.addLayout(middleLayout)
        windowLayout.addLayout(bottomLayout)

        window.setLayout(windowLayout)

        # Make window visible

        window.show()

        sys.exit(app.exec_())


mainWindow = MainWindow()
mainWindow()
