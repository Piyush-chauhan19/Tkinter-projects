import tkinter as tk

window = tk.Tk()
window.title("Experiment")
window.size()
window.minsize(200, 200)

# making the entry boxes
num1 = tk.IntVar()
number1 = tk.Entry(text=num1)
number1.grid(row=2, column=1)

num2 = tk.IntVar()
number1 = tk.Entry(text=num2)
number1.grid(row=2, column=3)


# making the functions

def add():
    result = float(num1.get()) + float(num2.get())
    ans.config(text=f"{result}")


def subtract():
    result = float(num1.get()) - float(num2.get())
    ans.config(text=f"{result}")


def product():
    result = float(num1.get()) * float(num2.get())
    ans.config(text=f"{result}")


def dividee():
    result = float(num1.get()) / float(num2.get())
    ans.config(text=f"{result}")


# making the button

plus = tk.Button(text="+", command=add)
plus.grid(row=1, column=2)
minus = tk.Button(text="-", command=subtract)
minus.grid(row=2, column=2)
multiply = tk.Button(text="*", command=product)
multiply.grid(row=3, column=2)
divide = tk.Button(text="/", command=dividee)
divide.grid(row=4, column=2)

# making the result box

answer = tk.Label(text="answer is : ")
answer.grid(row=5, column=1)
ans = tk.Label(text="0")
ans.grid(row=5, column=2)

window.mainloop()
