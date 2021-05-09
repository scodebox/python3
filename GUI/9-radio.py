from tkinter import *

root = Tk()
root.title('Radio')

# radio btn
gender = IntVar()


def f1():
    print(gender.get())
    Label(frame_1, text=gender.get()).pack()


# frame 1
frame_1 = LabelFrame(root, text='First', padx=50, pady=50)
frame_1.grid(row=0, column=0, padx=10, pady=10)


# radio btn
Radiobutton(frame_1, text="Male", variable=gender, value=1).pack(anchor=W)
Radiobutton(frame_1, text="Female", variable=gender, value=2).pack(anchor=W)

b1 = Button(frame_1, text='Submit', command=f1)
b1.pack()


# frame 2
frame_2 = LabelFrame(root, text='Second', padx=50, pady=50)
frame_2.grid(row=0, column=1, padx=10, pady=10)

# options
brand = [
    ('Apple', 'Apple'),
    ('Dell', 'Dell'),
    ('HP', 'HP'),
    ('Lenovo', 'lenovo'),
    ('Asus', 'Asus')
]

laptop = StringVar()
laptop.set('Apple')

# radio btn
for txt, val in brand:
    Radiobutton(frame_2, text=txt, variable=laptop, value=val).pack(anchor=W)


def f2():
    print(laptop.get())
    Label(frame_2, text=laptop.get()).pack()


b2 = Button(frame_2, text='Submit', command=f2)
b2.pack()


root.mainloop()
