from tkinter import *

root = Tk()
root.title('Frame')

# create frame
frame = LabelFrame(root, text='First frame', padx=50, pady=50)
# frame.pack(padx=10, pady=10)
frame.grid(row=0,column=0,padx=10, pady=10)

frame_t = LabelFrame(root, text='Second frame', padx=50, pady=50)
# frame_t.pack(padx=10, pady=10)
frame_t.grid(row=0,column=1,padx=10, pady=10)

# adding button in frame.
b1 = Button(frame, text='Submit')
b1.pack()
b2 = Button(frame, text='Check')
b2 .pack()

b3 = Button(frame_t, text='Another')
b3 .pack()

root.mainloop()
