from tkinter import *

root = Tk()
root.title('Checkbox')
root.geometry('200x200')


# checkbox 1
var = IntVar()


def check_1():
    print(var.get())


c1 = Checkbutton(root, text='Are you ready?', variable=var).pack()
Button(root, text='Get value', command=check_1).pack()


# checkbox 2
gate = StringVar()


def check_2():
    print(gate.get())


c2 = Checkbutton(root, text='Are you ready?', variable=gate,
                 onvalue='in', offvalue='out')
c2.deselect()
c2.pack()
Button(root, text='Get value', command=check_2).pack()

root.mainloop()
