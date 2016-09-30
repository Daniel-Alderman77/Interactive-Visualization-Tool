import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from numpy import arange, sin, pi

from FileHandler import ResponseDeserialization

# TODO - Implement Visualizer
# TODO - Implement line graphs
# TODO - Implement Guage plot
# TODO - Implement real-time plotting


class Visualizer:

    def __init__(self):
        self.name = self

    # TODO - Implement CPU graph
    # TODO - Implement Memory graph
    # TODO - Implement Jobs graph

    # TODO - Implement energy graph
    def draw_energy_graph(self, frame, row, column):
        response_deserialization = ResponseDeserialization()

        print response_deserialization.get_energy_visualizer_data()

        figure = Figure(figsize=(6, 5), dpi=60)
        subplot = figure.add_subplot(111)
        values = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * values)

        subplot.set_title('Tk embedding')
        subplot.set_xlabel('X axis label')
        subplot.set_ylabel('Y label')
        subplot.plot(values, s)

        # a tk.DrawingArea
        canvas = FigureCanvasTkAgg(figure, frame)
        canvas.show()
        canvas.get_tk_widget().grid(row=row, column=column)

    # TODO - Implement Latency graph
