from tkinter import *


root = Tk()
root.title('Dropdown')
root.geometry("300x100")


def show():
    print(selected.get())


options = [
    "Option 1",
    "Option 2",
    "Option 3",
    "Option 4",
    "Option 5",
    "Option 6"
]

# dropdown
selected = StringVar()
selected.set(options[0])

drop = OptionMenu(root, selected, *options)
drop.pack()

myButton = Button(root, text="Show", command=show).pack()

root.mainloop()
