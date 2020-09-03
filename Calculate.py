# _*_ coding: utf-8 _*_

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys

root = Tk()
root.title("Calculator")

#логика калькулятора
def calc(key):
    global memory
    if key == "=":
#исключение написание символов
        str1 = "-+0123456789.*/"
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")
#исчисления
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")
#Очищение поля
    elif key == "C":
        calc_entry.delete(0, END)
#Смена знака
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
#Exit
    elif key == "Exit":
        root.after(1, root.destroy)
        sys.exit
#Степень
    elif key == "^":
        calc_entry.insert(END, "**")
#!
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))
#()
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


#buttons
bttn_list = ["7", "8", "9", "+", "*", "4", "5", "6", "-",
             "/", "1", "2", "3", "=", "^", "0", ".", "±", "C", "Exit", "(", ")", "n!"]

r = 1
c = 0

for i in bttn_list:
    rel = ""
    cmd = lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 10).grid(row=r, column =c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width = 33)
calc_entry.grid(row = 0, column =0, columnspan = 5)

root.mainloop()