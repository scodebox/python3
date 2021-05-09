from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Images")
root.iconbitmap('demo.ico')

my_show = ImageTk.PhotoImage(Image.open("images/img1.png"))
label = Label(image=my_show)
label.pack()

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()
