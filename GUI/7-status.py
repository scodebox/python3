from tkinter import *

root = Tk()
root.title('With Status')
# text list
status = ['Text 1', 'Text 2', 'Text 3', 'Text 4', 'Text 5']
global index
index = 0

# text view
text_view = Label(root, text=status[index], width=30)
text_view.grid(row=0, column=0, columnspan=3)

# status view
status_view = Label(root, text=str(index+1), bd=1, relief=SUNKEN, anchor=W)
status_view.grid(row=2, column=0, columnspan=3, sticky=W+E)


# change next text
def move_left():
    global index
    index = (index-1) % len(status)

    text_view = Label(root, text=status[index], width=30)
    text_view.grid(row=0, column=0, columnspan=3)

    status_view = Label(root, text=str(index+1), bd=1, relief=SUNKEN, anchor=W)
    status_view.grid(row=2, column=0, columnspan=3, sticky=W+E)

# change prev text


def move_right():
    global index
    index = (index+1) % len(status)

    text_view = Label(root, text=status[index], width=30)
    text_view.grid(row=0, column=0, columnspan=3)

    status_view = Label(root, text=str(index+1), bd=1, relief=SUNKEN, anchor=W)
    status_view.grid(row=2, column=0, columnspan=3, sticky=W+E)


# left right button
left = Button(root, text="Left", command=move_left)
left.grid(row=1, column=0)
right = Button(root, text="Right", command=move_right)
right.grid(row=1, column=2)

root.mainloop()
