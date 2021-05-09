from tkinter import *
from tkinter import ttk

root = Tk()
root.title('ProgressBar')
root.geometry('400x300')

# Type 1
# def step():
#     progress['value'] += 20

# progress = ttk.Progressbar(root, orient=HORIZONTAL,
#    length = 300, mode = 'determinate')


# Type 2
def step():
    progress.start(20)


def stop():
    progress.stop()


# progress = ttk.Progressbar(root, orient=HORIZONTAL,
#                            length=300, mode='indeterminate')

progress = ttk.Progressbar(root, orient=HORIZONTAL,
                           length=300, mode='determinate')
progress.pack()

Button(root, text='Progress', command=step).pack()
Button(root, text='Stop', command=stop).pack()
root.mainloop()
