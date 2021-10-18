from tkinter import *
root = Tk()
root.title("PyCalculator")

E = Entry(root, width=40, borderwidth=5)
E.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

def numbtn(number):
    currentnum = E.get()
    E.delete(0, END)
    E.insert(0, str(currentnum) + str(number))

def clearbtn():
    E.delete(0, END)

def addbtn():
    firstnum = E.get()
    global num1
    global math
    math = "add"
    num1 = int(firstnum)
    E.delete(0, END)

def equalbtn():
    secondnum = E.get()
    E.delete(0, END)

    if math == "add":
        E.insert(0, num1 + int(secondnum))
    
    if math == "mul":
        E.insert(0, num1 * int(secondnum))
    
    if math == "sub":
        E.insert(0, num1 - int(secondnum))
    
    if math == "div":
        E.insert(0, num1 // int(secondnum))

def subbtn():
    firstnum = E.get()
    global num1
    global math
    math = "sub"
    num1 = int(firstnum)
    E.delete(0, END)

def divbtn():
    firstnum = E.get()
    global num1
    global math
    math = "div"
    num1 = int(firstnum)
    E.delete(0, END)
    
def mulbtn():
    firstnum = E.get()
    global num1
    global math
    math = "mul"
    num1 = int(firstnum)
    E.delete(0, END)

btn1 = Button(root, text="1", padx=35, pady=15, command=lambda: numbtn(1))
btn2 = Button(root, text="2", padx=35, pady=15, command=lambda: numbtn(2))
btn3 = Button(root, text="3", padx=35, pady=15, command=lambda: numbtn(3))
btn4 = Button(root, text="4", padx=35, pady=15, command=lambda: numbtn(4))
btn5 = Button(root, text="5", padx=35, pady=15, command=lambda: numbtn(5))
btn6 = Button(root, text="6", padx=35, pady=15, command=lambda: numbtn(6))
btn7 = Button(root, text="7", padx=35, pady=15, command=lambda: numbtn(7))
btn8 = Button(root, text="8", padx=35, pady=15, command=lambda: numbtn(8))
btn9 = Button(root, text="9", padx=35, pady=15, command=lambda: numbtn(9))
btn0 = Button(root, text="0", padx=35, pady=15, command=lambda: numbtn(0))
btnadd = Button(root, text="+", padx=35, pady=15, command=addbtn)
btnclear = Button(root, text="C", padx=80, pady=15, command=clearbtn)
btnequal = Button(root, text="=", padx=80, pady=15, command=equalbtn)
btnmul = Button(root, text="*", padx=35, pady=15, command=mulbtn)
btndiv = Button(root, text="/", padx=35, pady=15, command=divbtn)
btnsub = Button(root, text="-", padx=35, pady=15, command=subbtn)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn7.grid(row=3, column=0)
btn8.grid(row=3, column=1)
btn9.grid(row=3, column=2)
btn0.grid(row=4, column=0)
btnclear.grid(row=4, column=1, columnspan=2)
btnadd.grid(row=5, column=0)
btnequal.grid(row=5, column=1, columnspan=2)
btnsub.grid(row=6, column=0)
btnmul.grid(row=6, column=1)
btndiv.grid(row=6, column=2)

root.mainloop()
