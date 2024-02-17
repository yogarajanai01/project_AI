import tkinter
from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("checking colour")
top.geometry("300x150")
top.state("zoomed")
top.config(bg="pale green")
def clickyellow():
    messagebox.showinfo("Hello", "yellow Button clicked")
a = Button(top, text="yellow",  command=clickyellow,activeforeground="yellow", activebackground="orange", pady=10, bg="yellow")
def clickblue():
    messagebox.showinfo("Hello","Blue button is clicked")
b = Button(top, text="Blue",  command=clickblue,activeforeground="blue", activebackground="orange", pady=10 , bg="blue")
def clickgreen():
    messagebox.showinfo("Hello","Green button is clicked")
c = Button(top, text="Green", command=clickgreen, activeforeground = "green", activebackground="orange", pady=10 , bg="green")
def clickred():
    messagebox.showinfo("Hello","Red button is clicked")
d = Button(top, text="red",  command=clickred,activeforeground="yellow", activebackground="orange", pady=10, bg="red")

a.pack(side = RIGHT)
b.pack(side = LEFT)
c.pack(side = TOP)
d.pack(side = BOTTOM)
top.mainloop()

