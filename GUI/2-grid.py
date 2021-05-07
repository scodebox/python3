from tkinter import *

root = Tk()

# Creating label widget
my_label_1 = Label(root, text="Hello")
my_label_2 = Label(root, text="World!")
my_label_3 = Label(root, text="Test")

my_label_1.grid(row=0, column=0)
my_label_2.grid(row=1, column=1)
my_label_3.grid(row=2, column=2)


######## OR ###########

# Label(root, text="Hello").grid(row=0, column=0)
# Label(root, text="World!").grid(row=1, column=1)
# Label(root, text="Test").grid(row=2, column=2)


root.mainloop()
