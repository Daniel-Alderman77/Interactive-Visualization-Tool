from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from numpy import arange, sin, pi

# TODO - Implement Visualizer
# TODO - Implement line graphs
# TODO - Implement Guage plot
# TODO - Implement real-time plotting


class Visualizer:

    def __init__(self):
        self.name = self

    def draw_graph(self, frame, row, column):
        figure = Figure(figsize=(3, 2), dpi=100)
        subplot = figure.add_subplot(111)
        values = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * values)

        subplot.plot(values, s)

        # a tk.DrawingArea
        canvas = FigureCanvasTkAgg(figure, frame)
        canvas.show()
        canvas.get_tk_widget().grid(row=row, column=column)
