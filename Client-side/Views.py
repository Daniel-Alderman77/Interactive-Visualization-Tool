from Tkinter import Frame, Button, Toplevel, Tk, LEFT


class MainView:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.button1 = Button(self.frame, text='New Window', width=25, command=self.new_window)
        self.button2 = Button(self.frame, text='New Window', width=25, command=self.new_window)
        self.button3 = Button(self.frame, text='New Window', width=25, command=self.new_window)
        self.button1.pack(side=LEFT)
        self.button2.pack(side=LEFT)
        self.button3.pack(side=LEFT)
        self.frame.pack()

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = SubView(self.newWindow)


class SubView():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.quitButton = Button(self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


def main():
    root = Tk()
    app = MainView(root)
    root.mainloop()

if __name__ == '__main__':
    main()
