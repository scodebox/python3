from tkinter import *

root = Tk()
root.title("Calculator")

# input show
text_input = Entry(root, borderwidth=1)
text_input.grid(row=0, column=0, columnspan=3)

# functions


def button_click(number): 
    text_input.insert(END, number)


def clear():
    text_input.delete(0, END)


def operation(symbol):
    global current_operation, number_1
    current_operation = symbol
    number_1 = int(text_input.get())
    clear()


def result():
    number_2 = int(text_input.get())
    clear()
    if current_operation == '+':
        text_input.insert(0, number_1+number_2)
    elif current_operation == '-':
        text_input.insert(0, number_1-number_2)
    elif current_operation == '*':
        text_input.insert(0, number_1*number_2)
    elif current_operation == '/':
        text_input.insert(0, number_1/number_2)
    else:
        text_input.insert(0, 'ERROR')


# Buttons
button_0 = Button(root, text="0", command=lambda: button_click(0))
button_1 = Button(root, text="1", command=lambda: button_click(1))
button_2 = Button(root, text="2", command=lambda: button_click(2))
button_3 = Button(root, text="3", command=lambda: button_click(3))
button_4 = Button(root, text="4", command=lambda: button_click(4))
button_5 = Button(root, text="5", command=lambda: button_click(5))
button_6 = Button(root, text="6", command=lambda: button_click(6))
button_7 = Button(root, text="7", command=lambda: button_click(7))
button_8 = Button(root, text="8", command=lambda: button_click(8))
button_9 = Button(root, text="9", command=lambda: button_click(9))


button_add = Button(root, text="+", command=lambda: operation('+'))
button_subs = Button(root, text="-", command=lambda: operation('-'))
button_mult = Button(root, text="x", command=lambda: operation('*'))
button_div = Button(root, text="/", command=lambda: operation('/'))

button_equal = Button(root, text="=", command=result)
button_clear = Button(root, text="C", command=clear, width=10)

# place buttons
button_0.grid(row=5, column=0)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_clear.grid(row=1, column=1, columnspan=2)
button_add.grid(row=5, column=1)
button_subs.grid(row=5, column=2)
button_mult.grid(row=6, column=1)
button_div.grid(row=6, column=2)
button_equal.grid(row=6, column=0)


root.mainloop()
