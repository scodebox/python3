from tkinter import *
from tkinter import filedialog


root = Tk()
root.title('Open File')


def file_open():
    root.filename = filedialog.askopenfilename(initialdir='/Users/suvambasak/Documents', title='Select file', filetypes=(
        ("pdf files", "*.pdf"), ("all files", "*.*")))
    print(root.filename)


Button(root, text='Open', command=file_open).pack()


root.mainloop()
