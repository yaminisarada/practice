#simeple GUI

from tkinter import *

#create the window
root = Tk()


#modify root window
root.title("Simple Gui")
root.geometry("800x600")

def hellocall():
    print("Hello GUI")
#button1 = Button(app, text ="
B = Tk.Button(top, text ="Hello", command = helloCallBack)
B.pack()
#kick off the event loop
root.mainloop()

