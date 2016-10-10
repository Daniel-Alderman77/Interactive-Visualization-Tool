import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import animation


from Tkinter import BOTTOM, Tk, Toplevel, HORIZONTAL
# Override the basic Tk widgets, with platform specific widgets
from tkinter.ttk import *
from Visualizer import Visualizer, LineGraph, EnergyGraph, LatencyGraph


# TODO - Display percentage progress through number of remote files
class MainView:
    def __init__(self, master):
        visualizer = Visualizer()

        self.master = master

        self.frame = Frame(self.master)

        self.bottom_frame = Frame(self.master)
        self.bottom_frame.pack(side=BOTTOM)

        self.cpu_button = Button(self.frame, text='CPU Utilisation', width=25, command=self.cpu_view)
        self.cpu_button.grid(row=0, column=0)

        line_graph = LineGraph()

        # tk.DrawingArea
        canvas = FigureCanvasTkAgg(line_graph.fig, self.frame)

        # call the animator
        anim = animation.FuncAnimation(line_graph.fig, line_graph.animate, init_func=line_graph.init, frames=200,
                                       interval=1000, blit=False)

        canvas.show()
        canvas.get_tk_widget().grid(row=1, column=0)

        self.memory_button = Button(self.frame, text='Memory Utilisation', width=25, command=self.memory_view)
        self.memory_button.grid(row=0, column=1)

        self.memory_graph = visualizer.draw_energy_graph(self.frame, 1, 1)

        self.jobs_button = Button(self.frame, text='Current Jobs', width=25, command=self.jobs_view)
        self.jobs_button.grid(row=2, column=0)

        self.jobs_graph = visualizer.draw_energy_graph(self.frame, 3, 0)

        self.energy_button = Button(self.frame, text='Energy View', width=25, command=self.energy_view)
        self.energy_button.grid(row=2, column=1)

        energy_graph = EnergyGraph()

        # tk.DrawingArea
        canvas = FigureCanvasTkAgg(energy_graph.fig, self.frame)

        # call the animator
        anim = animation.FuncAnimation(energy_graph.fig, energy_graph.animate, init_func=energy_graph.init, frames=200,
                                       interval=1000, blit=False)

        canvas.show()
        canvas.get_tk_widget().grid(row=3, column=1)

        self.latency_button = Button(self.bottom_frame, text='Faults', width=25, command=self.faults_view)
        self.latency_button.grid(row=5, column=0)

        latency_graph = LatencyGraph()

        # tk.DrawingArea
        canvas = FigureCanvasTkAgg(latency_graph.fig, self.frame)

        # call the animator
        anim = animation.FuncAnimation(latency_graph.fig, latency_graph.animate, init_func=latency_graph.init, frames=200,
                                       interval=1000, blit=False)

        canvas.show()
        canvas.get_tk_widget().grid(row=5)

        self.frame.pack()

    def cpu_view(self):
        self.new_window = Toplevel(self.master)
        self.app = CPUView(self.new_window)

    def memory_view(self):
        self.new_window = Toplevel(self.master)
        self.app = MemoryView(self.new_window)

    def jobs_view(self):
        self.new_window = Toplevel(self.master)
        self.app = JobsView(self.new_window)

    def energy_view(self):
        self.new_window = Toplevel(self.master)
        self.app = EnergyView(self.new_window)

    def faults_view(self):
        self.new_window = Toplevel(self.master)
        self.app = FaultsView(self.new_window)


class SubView:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.close_button = Button(self.frame, text='Close', width=25, command=self.close_window)
        self.close_button.pack()

        self.frame.pack()

    def close_window(self):
        self.master.destroy()


# TODO - Implement CPUView UI
class CPUView(SubView):
    def __init__(self, master):
        SubView.__init__(self, master)
        self.close_button = Button(self.frame, text='CpuView', width=25, command=self.close_window)
        self.close_button.pack()


# TODO - Implement MemoryView UI
class MemoryView(SubView):
    def __init__(self, master):
        SubView.__init__(self, master)
        self.close_button = Button(self.frame, text='MemoryView', width=25, command=self.close_window)
        self.close_button.pack()


# TODO - Implement JobsView UI
class JobsView(SubView):
    def __init__(self, master):
        SubView.__init__(self, master)
        self.close_button = Button(self.frame, text='JobsView', width=25, command=self.close_window)
        self.close_button.pack()


# TODO - Implement EnergyView UI
class EnergyView(SubView):
    def __init__(self, master):
        SubView.__init__(self, master)
        self.close_button = Button(self.frame, text='EnergyView', width=25, command=self.close_window)
        self.close_button.pack()


# TODO - Implement FaultsView UI
class FaultsView(SubView):
    def __init__(self, master):
        SubView.__init__(self, master)
        progress_bar = Progressbar(self.frame, orient=HORIZONTAL, length=600, mode='determinate')
        progress_bar.pack()
        progress_bar["maximum"] = 100
        progress_bar["value"] = 50


class UserInterface:

    def __init__(self):
        self.name = self

    def run(self):
        root = Tk()
        app = MainView(root)
        root.title('Interactive Visualization Tool')

        return root

    def main_loop(self, root):
        root.mainloop()
