from tkinter import *

root = Tk()


# Creating input
text_input = Entry(root)
text_input.pack()
# default text
text_input.insert(0, "Enter here!")


def click():
    my_label = Label(root, text=text_input.get())
    my_label.pack()


button_1 = Button(root, text="Submit", command=click)
button_1.pack()

root.mainloop()
