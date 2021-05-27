from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

delete = 0
operator = "None"
f_num = None
ans = None

def button_click(number):
    if str(e.get()) == "+" or str(e.get()) == "-" or str(e.get()) == "*" or str(e.get()) == "/":
        e.delete(0, END)
    if operator == "None":
        current = ""
        change_operator("NA")
    else:
        current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)
    global total
    global operator
    f_num = 0
    operator = "None"


def button_add():
    current_number = int(e.get())
    global f_num
    if f_num is None:
        f_num = current_number
    else:
        f_num = find_total(current_number)
    change_operator("add")
    e.delete(0, END)
    e.insert(0, "+")


def button_subtract():
    current_number = int(e.get())
    global f_num
    if f_num is None:
        f_num = current_number
    else:
        f_num = find_total(current_number)
    change_operator("subtract")
    e.delete(0, END)
    e.insert(0, "-")


def button_multiply():
    current_number = int(e.get())
    global f_num
    if f_num is None:
        f_num = current_number
    else:
        f_num = find_total(current_number)
    change_operator("multiply")
    e.delete(0, END)
    e.insert(0, "*")


def button_divide():
    current_number = int(e.get())
    global f_num
    if f_num is None:
        f_num = current_number
    else:
        f_num = find_total(current_number)
    change_operator("divide")
    e.delete(0, END)
    e.insert(0, "/")


def button_equal():
    global total
    current = int(e.get())
    e.delete(0, END)
    loc_total = final_total(current)
    e.insert(0, loc_total)
    f_num = None
    operator = "None"
    global ans
    ans = loc_total


def button_ans():
    e.delete(0, END)
    e.insert(0, str(ans))


def find_total(current):
    if operator == "add":
        loc_total = current + f_num
    elif operator == "subtract":
        loc_total = f_num - current
    elif operator == "multiply":
        loc_total = current * f_num
    elif operator == "divide":
        try:
            loc_total = f_num / current
        except ZeroDivisionError:
            loc_total = "Error"
    elif operator == "None" or operator == "NA":
        return current
    change_operator("None")
    return loc_total


def final_total(current):
    if operator == "add":
        loc_total = current + f_num
    elif operator == "subtract":
        loc_total = f_num - current
    elif operator == "multiply":
        loc_total = current * f_num
    elif operator == "divide":
        try:
            loc_total = f_num / current
        except ZeroDivisionError:
            loc_total = "Error"
    change_operator("None")
    return loc_total


def change_operator(new):
    global operator
    operator = new




# define buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=88, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=30, pady=20, command=button_clear)
button_ans = Button(root, text="ans", padx=34, pady=20, command=button_ans)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)

# put buttons on screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4,column=1)
button_ans.grid(row=4, column=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5,column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


root.mainloop()
