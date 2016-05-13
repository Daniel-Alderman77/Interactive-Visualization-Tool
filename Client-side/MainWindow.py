import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QGroupBox, QFont, QLabel, QVBoxLayout, QHBoxLayout, QMainWindow
import matplotlib

matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4'] = 'PySide'

# Warnings need to be ignored to preserve import order
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class MainWindow:
    def __init__(self):
        self.name = self

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

        cpu_label = QLabel()
        cpu_label.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
        cpu_label.setAlignment(Qt.AlignCenter)
        cpu_label.setText("CPU Utilisation")

        memory_label = QLabel()
        memory_label.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
        memory_label.setAlignment(Qt.AlignCenter)
        memory_label.setText("Memory Utilisation")

        jobs_label = QLabel()
        jobs_label.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
        jobs_label.setAlignment(Qt.AlignCenter)
        jobs_label.setText("Current Jobs")

        hierarchy_label = QLabel()
        hierarchy_label.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
        hierarchy_label.setAlignment(Qt.AlignCenter)
        hierarchy_label.setText("Hierarchy View")

        latency_label = QLabel()
        latency_label.setFont(QFont("DejaVu Sans Mono", 28, QFont.Bold))
        latency_label.setAlignment(Qt.AlignCenter)
        latency_label.setText("Latency")

        # Top Layout

        top_layout = QHBoxLayout()

        top_left_layout = QVBoxLayout()
        top_left_layout.addWidget(cpu_label)
        top_left_layout.addWidget(self.cpu_figure())

        top_right_layout = QVBoxLayout()
        top_right_layout.addWidget(memory_label)
        top_right_layout.addWidget(self.cpu_figure())

        top_layout.addLayout(top_left_layout)
        top_layout.addLayout(top_right_layout)

        # Middle Layout

        middle_layout = QHBoxLayout()

        middle_left_layout = QVBoxLayout()
        middle_left_layout.addWidget(jobs_label)
        middle_left_layout.addWidget(self.cpu_figure())

        middle_right_layout = QVBoxLayout()
        middle_right_layout.addWidget(hierarchy_label)
        middle_right_layout.addWidget(self.cpu_figure())

        middle_layout.addLayout(middle_left_layout)
        middle_layout.addLayout(middle_right_layout)

        # Bottom layout

        bottom_layout = QVBoxLayout()
        bottom_layout.addWidget(latency_label)
        bottom_layout.addWidget(self.cpu_figure())

        # Stack layouts on top of each other

        window_layout = QVBoxLayout()
        window_layout.addLayout(top_layout)
        window_layout.addLayout(middle_layout)
        window_layout.addLayout(bottom_layout)

        window.setLayout(window_layout)

        # Make window visible

        window.show()

        sys.exit(app.exec_())

mainWindow = MainWindow()
mainWindow()
