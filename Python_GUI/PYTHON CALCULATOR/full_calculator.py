from tkinter import *


def btn(numbers):
    global operator
    operator += str(numbers)
    txt_input.set(operator)


def Clear():
    global operator
    operator = ""
    txt_input.set("")
    Display.insert(0, "Start Calculating...")


def Del():
    global operator
    operator = operator[:-1]
    txt_input.set(operator)


def Equal():
    global operator
    sumup = float(eval(operator))
    txt_input.set(sumup)
    operator = ""


root = Tk()
root.title("Calculator")

operator = ""
txt_input = StringVar(value="Start Calculating...")

# ======================================Screen==================================
Display = Entry(
    root,
    font=("arial", 28, "bold"),
    fg="white",
    bg="green",
    justify="right",
    bd=40,
    textvariable=txt_input,
)

Display.grid(columnspan=4)

# ======================================Row1====================================
btn7 = Button(
    root,
    padx=28,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="7",
    command=lambda: btn(7),
).grid(row=1, column=0)

btn8 = Button(
    root,
    padx=28,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="8",
    command=lambda: btn(8),
).grid(row=1, column=1)

btn9 = Button(
    root,
    padx=28,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="9",
    command=lambda: btn(9),
).grid(row=1, column=2)

btndel = Button(
    root,
    padx=22,
    pady=14,
    bd=6,
    fg="black",
    font=(
        "arial",
        26,
    ),
    text="<<",
    bg="red",
    command=Del,
).grid(row=1, column=3)

# ======================================Row2====================================
btn4 = Button(
    root,
    padx=28,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="4",
    command=lambda: btn(4),
).grid(row=2, column=0)

btn5 = Button(
    root,
    padx=28,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="5",
    command=lambda: btn(5),
).grid(row=2, column=1)

btn6 = Button(
    root,
    padx=28,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="6",
    command=lambda: btn(6),
).grid(row=2, column=2)

btnplus = Button(
    root,
    padx=31,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="+",
    bg="orange",
    command=lambda: btn("+"),
).grid(row=2, column=3)

# ======================================Row3====================================
btn1 = Button(
    root,
    padx=28,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="1",
    command=lambda: btn(1),
).grid(row=3, column=0)

btn2 = Button(
    root,
    padx=28,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="2",
    command=lambda: btn(2),
).grid(row=3, column=1)

btn3 = Button(
    root,
    padx=28,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="3",
    command=lambda: btn(3),
).grid(row=3, column=2)

btnMinus = Button(
    root,
    padx=36,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="-",
    bg="orange",
    command=lambda: btn("-"),
).grid(row=3, column=3)

# ======================================Row4====================================
btn0 = Button(
    root,
    padx=28,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="0",
    command=lambda: btn(0),
).grid(row=4, column=0)

btndot = Button(
    root,
    padx=33,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text=".",
    bg="orange",
    command=lambda: btn("."),
).grid(row=4, column=1)

btndiv = Button(
    root,
    padx=34,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="/",
    bg="orange",
    command=lambda: btn("/"),
).grid(row=4, column=2)

btnmul = Button(
    root,
    padx=32,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="x",
    bg="orange",
    command=lambda: btn("*"),
).grid(row=4, column=3)

# ======================================Row5====================================
btnEqu = Button(
    root,
    padx=28,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="=",
    bg="green",
    command=Equal,
).grid(row=5, column=0)

btnopenBrac = Button(
    root,
    padx=33,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="(",
    bg="blue",
    command=lambda: btn("("),
).grid(row=5, column=1)

btncloseBrac = Button(
    root,
    padx=34,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text=")",
    bg="blue",
    command=lambda: btn(")"),
).grid(row=5, column=2)

btnC = Button(
    root,
    padx=28,
    pady=14,
    bd=6,
    fg="black",
    font=("arial", 26, "bold"),
    text="C",
    bg="green",
    command=Clear,
).grid(row=5, column=3)

root.mainloop()
