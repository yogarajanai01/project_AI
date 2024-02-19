from tkinter import *
from tkinter import ttk

data=Tk()

data.title("Databases for STD MARKS")
data.geometry("500x500+500+100")
data.state("zoomed")
data.config(bg="lightgreen")

def insert():
    pass
def update():
    pass
def delete():
    pass
def reset():
    pass
def truncate():
    pass


labelname=Label(data,text="NAME")
labelname.grid(row=0,column=50,padx=20,pady=20)
labelname.config(bg="black",fg="white")

inputName=Entry(data,text="")
inputName.grid(row=0,column=100)
inputName.config(bg="black",fg="white")

labelroll=Label(data,text="ROLL_NO")
labelroll.grid(row=2,column=50,padx=20,pady=20)
labelroll.config(bg="black",fg="white")

inputroll=Entry(data,text="")
inputroll.grid(row=2,column=100)
inputroll.config(bg="black",fg="white")

TAM=Label(data,text="TAMIL")
TAM.grid(row=10,column=50,padx=20,pady=20)
TAM.config(bg="black",fg="white")

inputt=Entry(data,text="")
inputt.grid(row=10,column=100)
inputt.config(bg="black",fg="white")

ENG=Label(data,text="ENGLISH")
ENG.grid(row=12,column=50,padx=20,pady=20)
ENG.config(bg="black",fg="white")

inputE=Entry(data,text="")
inputE.grid(row=12,column=100)
inputE.config(bg="black",fg="white")

MATH=Label(data,text="MATHS")
MATH.grid(row=14,column=50,padx=20,pady=20)
MATH.config(bg="black",fg="white")

inputM=Entry(data,text="")
inputM.grid(row=14,column=100)
inputM.config(bg="black",fg="white")

PHY=Label(data,text="PHYSICS")
PHY.grid(row=16,column=50,padx=20,pady=20)
PHY.config(bg="black",fg="white")

inputP=Entry(data,text="")
inputP.grid(row=16,column=100)
inputP.config(bg="black",fg="white")

insbut=Button(data,text="INSERT")
insbut.grid(row=25,column=20,padx=40,pady=40)
insbut.config(bg="blue")

insbut=Button(data,text="UPDATE")
insbut.grid(row=25,column=50,padx=40,pady=40)
insbut.config(bg="green")

insbut=Button(data,text="DELETE")
insbut.grid(row=25,column=80,padx=40,pady=40)
insbut.config(bg="red")

insbut=Button(data,text="RESET")
insbut.grid(row=25,column=150,padx=40,pady=40)
insbut.config(bg="orange")

insbut=Button(data,text="TRUNCATE")
insbut.grid(row=25,column=250,padx=40,pady=40)
insbut.config(bg="dark red")

labelouptut=Label(data,text="",bg="black",fg="white")
labelouptut.grid(row=40,column=20,)

mainloop()






