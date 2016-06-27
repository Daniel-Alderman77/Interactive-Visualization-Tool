from Tkinter import Frame, Button, Toplevel, Tk, LEFT, BOTTOM, TOP


class MainView:
    def __init__(self, master):
        self.master = master

        self.frame = Frame(self.master)

        self.top_frame = Frame(self.master)
        self.top_frame.pack(side=TOP)

        self.bottom_frame = Frame(self.master)
        self.bottom_frame.pack(side=BOTTOM)

        self.cpu_button = Button(self.top_frame, text='CPU Utilisation', width=25, command=self.cpu_view)
        self.cpu_button.pack(side=LEFT)

        self.memory_button = Button(self.top_frame, text='Memory Utilisation', width=25, command=self.memory_view)
        self.memory_button.pack(side=LEFT)

        self.jobs_button = Button(self.frame, text='Current Jobs', width=25, command=self.jobs_view)
        self.jobs_button.pack(side=LEFT)

        self.hier_button = Button(self.frame, text='Hierarchical View', width=25, command=self.hier_view)
        self.hier_button.pack(side=LEFT)

        self.latency_button = Button(self.bottom_frame, text='Latency', width=25, command=self.latency_view)
        self.latency_button.pack(side=BOTTOM)

        self.frame.pack()

    def cpu_view(self):
        self.new_window = Toplevel(self.master)
        self.app = CpuView(self.new_window)

    def memory_view(self):
        self.new_window = Toplevel(self.master)
        self.app = MemoryView(self.new_window)

    def jobs_view(self):
        self.new_window = Toplevel(self.master)
        self.app = JobsView(self.new_window)

    def hier_view(self):
        self.new_window = Toplevel(self.master)
        self.app = HierView(self.new_window)

    def latency_view(self):
        self.new_window = Toplevel(self.master)
        self.app = LatencyView(self.new_window)


class SubView:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.close_button = Button(self.frame, text='Close', width=25, command=self.close_window)
        self.close_button.pack()
        self.frame.pack()

    def close_window(self):
        self.master.destroy()


class CpuView(SubView):
    def __init__(self, master):
        SubView.__init__(self, master)
        self.close_button = Button(self.frame, text='CpuView', width=25, command=self.close_window)
        self.close_button.pack()


class MemoryView(SubView):
    def __init__(self, master):
        SubView.__init__(self, master)
        self.close_button = Button(self.frame, text='MemoryView', width=25, command=self.close_window)
        self.close_button.pack()


class JobsView(SubView):
    def __init__(self, master):
        SubView.__init__(self, master)
        self.close_button = Button(self.frame, text='JobsView', width=25, command=self.close_window)
        self.close_button.pack()


class HierView(SubView):
    def __init__(self, master):
        SubView.__init__(self, master)
        self.close_button = Button(self.frame, text='HierView', width=25, command=self.close_window)
        self.close_button.pack()


class LatencyView(SubView):
    def __init__(self, master):
        SubView.__init__(self, master)
        self.close_button = Button(self.frame, text='LatencyView', width=25, command=self.close_window)
        self.close_button.pack()


def main():
    root = Tk()
    app = MainView(root)
    root.title('Interactive Visualization Tool')
    root.mainloop()

if __name__ == '__main__':
    main()
