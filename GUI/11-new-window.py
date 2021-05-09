from tkinter import *


root = Tk()
root.title('First Window')


def new_window():
    top = Toplevel()
    top.title('Second Window')
    Button(top, text='Quit', command=top.destroy).pack()


Button(root, text='New window', command=new_window).pack()


root.mainloop()
