'''import tkinter as tk

menu=tk.Tk()
menu.geometry("500x500")
menu.title("NOTEPAD.007")

def quit():
    menu.destroy()

def aboutpage():
    abt=tk.Tk()
    abt.title("About us")
    abt.geometry("300x300")
    message="""Welcome to NOTEPAD.007
    created on : 22-02-2024
    by Yoga The AITECH.
    """
    lntinfo=tk.Label(abt,text=message)
    lntinfo.pack()
    abt.mainloop()    



def New():
    menu=tk.Tk()
    menu.geometry("500x500")
    menu.title("untitled.1")
    menubar=tk.Menu(menu)
    filemenu=tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=filemenu,underline=0)
    filemenu.add_command(label="New     Ctrl+N",underline=0,command=New)
    filemenu.add_command(label="New Window      Ctrl+W",underline=4,command=New_Window)
    filemenu.add_command(label="Open        Ctrl+O",underline=0)
    filemenu.add_command(label="Save        Ctrl+S",underline=0)
    filemenu.add_command(label="Save As     Ctrl+A",underline=5)
    filemenu.add_separator()
    filemenu.add_command(label="Page Setup      Ctrl+P",underline=0)
    filemenu.add_command(label="Print       Ctrl+r",underline=1)
    filemenu.add_separator()
    filemenu.add_command(label="Exit        Ctrl+E",underline=0,command=quit)

    editmenu=tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit",menu=editmenu)
    editmenu.add_command(label="Undo",  underline=0, accelerator="Alt+F")
    editmenu.add_command(label="Redo",  underline=4, accelerator="Alt+F")
    editmenu.add_separator()
    editmenu.add_command(label="Copy",  underline=0, accelerator="Alt+F")
    editmenu.add_command(label="Cut",  underline=0, accelerator="Alt+F")
    editmenu.add_command(label="Paste",  underline=0, accelerator="Alt+F")
    
    viewmenu=tk.Menu(menubar)
    menubar.add_cascade(label="View")

    helpmenu=tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Help",menu=helpmenu)
    helpmenu.add_command(label="About",  underline=0, accelerator="Alt+F", command=aboutpage)
    menu.config(menu=menubar)

    text_widget = tk.Text(menu, wrap=tk.WORD)
    text_widget.pack(fill=tk.BOTH, expand=True)


def New_Window():
    menu=tk.Tk()
    menu.geometry("500x500")
    menu.title("NOTEPAD.007")
    menubar=tk.Menu(menu)
    filemenu=tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=filemenu,underline=0)
    filemenu.add_command(label="New     Ctrl+N",underline=0,command=New)
    filemenu.add_command(label="New Window      Ctrl+W",underline=4,command=New_Window)
    filemenu.add_command(label="Open        Ctrl+O",underline=0)
    filemenu.add_command(label="Save        Ctrl+S",underline=0)
    filemenu.add_command(label="Save As     Ctrl+A",underline=5)
    filemenu.add_separator()
    filemenu.add_command(label="Page Setup      Ctrl+P",underline=0)
    filemenu.add_command(label="Print       Ctrl+r",underline=1)
    filemenu.add_separator()
    filemenu.add_command(label="Exit        Ctrl+E",underline=0,command=quit)

    editmenu=tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit",menu=editmenu)
    editmenu.add_command(label="Undo",  underline=0, accelerator="Alt+F")
    editmenu.add_command(label="Redo",  underline=4, accelerator="Alt+F")
    editmenu.add_separator()
    editmenu.add_command(label="Copy",  underline=0, accelerator="Alt+F")
    editmenu.add_command(label="Cut",  underline=0, accelerator="Alt+F")
    editmenu.add_command(label="Paste",  underline=0, accelerator="Alt+F")
    
    viewmenu=tk.Menu(menubar)
    menubar.add_cascade(label="View")

    helpmenu=tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Help",menu=helpmenu)
    helpmenu.add_command(label="About",  underline=0, accelerator="Alt+F", command=aboutpage)
    menu.config(menu=menubar)

    
                                                                           

menubar=tk.Menu(menu)
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu,underline=0)
filemenu.add_command(label="New     Ctrl+N",underline=0,command=New)
filemenu.add_command(label="New Window      Ctrl+W",underline=4,command=New_Window)
filemenu.add_command(label="Open        Ctrl+O",underline=0)
filemenu.add_command(label="Save        Ctrl+S",underline=0)
filemenu.add_command(label="Save As     Ctrl+A",underline=5)
filemenu.add_separator()
filemenu.add_command(label="Page Setup      Ctrl+P",underline=0)
filemenu.add_command(label="Print       Ctrl+r",underline=1)
filemenu.add_separator()
filemenu.add_command(label="Exit        Ctrl+E",underline=0,command=quit)

editmenu=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Undo",  underline=0, accelerator="Alt+F")
editmenu.add_command(label="Redo",  underline=4, accelerator="Alt+F")
editmenu.add_separator()
editmenu.add_command(label="Copy",  underline=0, accelerator="Alt+F")
editmenu.add_command(label="Cut",  underline=0, accelerator="Alt+F")
editmenu.add_command(label="Paste",  underline=0, accelerator="Alt+F")

viewmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="View")
viewmenu.add_command(label="status bar",accelerator="ctrl+s")

helpmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="About",  underline=0, accelerator="Alt+F", command=aboutpage)
menu.config(menu=menubar)

menu.mainloop()'''


import turtle

s = turtle.Screen().bgcolor("white")
t = turtle.Turtle()
t.speed(10)
t.width(12)

def curve():
    for i in range (200):
        t.right(1)
        t.forward(1)

def heart():
    t.color("red","red")
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

heart()
t.pencolor("black")
t.penup()
t.goto(0,170)
t.pendown()

for broken in range (3):
    t.left(75)
    t.forward(40)
    t.right(65)
    t.forward(45)

turtle.done()