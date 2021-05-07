from tkinter import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # add stuff to the window
        self.add_stuff()

    def add_stuff(self):
        # add title
        self.master.title("GUP App")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        # button
        quit_button = Button(self, text="Quit", command=self.window_exit)
        quit_button.place(x=0, y=0)

    def window_exit(self):
        exit()


root = Tk()
# size of window
root.geometry("400x300")

Window(root)
root.mainloop()
