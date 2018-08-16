# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def hello():
   messagebox.showinfo("Your Name", "Hello World")

B1 = Button(top, text = "Your Name", command = hello)
B1.place(x = 35,y = 50)

top.mainloop()
