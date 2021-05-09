from tkinter import *
from tkinter import messagebox as msgbox

root = Tk()
root.title('Message Box')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def showinfo():
    response = msgbox.showinfo("Popup", "Hello World!")
    print(response)


def showwarning():
    response = msgbox.showwarning("Popup", "Hello World!")
    print(response)


def showerror():
    response = msgbox.showerror("Popup", "Hello World!")
    print(response)


def askquestion():
    response = msgbox.askquestion("Popup", "Hello World!")
    print(response)


def askokcancel():
    response = msgbox.askokcancel("Popup", "Hello World!")
    print(response)


def askyesno():
    response = msgbox.askyesno("Popup", "Hello World!")
    print(response)


Button(root, text="show info", command=showinfo).pack()
Button(root, text="show warning", command=showwarning).pack()
Button(root, text="show error", command=showerror).pack()
Button(root, text="ask question", command=askquestion).pack()
Button(root, text="ask ok cancel", command=askokcancel).pack()
Button(root, text="ask yes no", command=askyesno).pack()

root.mainloop()
