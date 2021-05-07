from tkinter import *

root = Tk()


def click():
    my_label = Label(root, text="Suvam Basak!")
    my_label.pack()


# Creating button
button_1 = Button(root, text="Click Me 1").pack()

button_2 = Button(root, text="Click Me 2", state=DISABLED).pack()

button_3 = Button(root, text="Click Me 3", padx=50, pady=40).pack()

button_4 = Button(root, text="Click Me 4", command=click).pack()

button_5 = Button(root, text="Click Me 5", bg="blue", fg="red").pack()


root.mainloop()
