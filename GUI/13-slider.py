from tkinter import *

root = Tk()
root.title('Sliders')
root.geometry('200x200')

# slider
vertical = Scale(root, from_=200, to=1000)
vertical.pack()
horizontal = Scale(root, from_=200, to=1000, orient=HORIZONTAL)
horizontal.pack()


def setup():
    root.geometry(str(horizontal.get())+'x'+str(vertical.get()))


Button(root, text='Change', command=setup).pack()
root.mainloop()
