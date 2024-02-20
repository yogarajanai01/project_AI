from tkinter import *
import mysql.connector


data=Tk()

data.title("Databases for STD MARKS")
data.geometry("500x500+500+100")
data.state("zoomed")
data.config(bg="lightblue")


def Mydbconnection():
    dbcon=mysql.connector.connect(
    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_yogarajan"
    )

    return dbcon


def insert():
    valuename=str(inputName.get())
    valueRollNo=int(inputroll.get())
    valuetam=int(inputt.get())
    valueeng=int(inputE.get())
    valuemath=int(inputM.get())
    valuephy=int(inputP.get())

    e_con=Mydbconnection()
    result=e_con.cursor()

    statement="insert into STD_MARKS (Name,Roll_No,TAMIL,ENGLISH,MATHS,PHYSICS) VALUES (%s,%s,%s,%s,%s,%s);"
    valuepass=(valuename,valueRollNo,valuetam,valueeng,valuemath,valuephy)
    result.execute(statement,valuepass)
    e_con.commit()

    print(result.rowcount, " row inserted")

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
labelname.config(bg="blue",fg="white")

inputName=Entry(data)
inputName.grid(row=0,column=100)
inputName.config(bg="blue",fg="white")

labelroll=Label(data,text="ROLL_NO")
labelroll.grid(row=2,column=50,padx=20,pady=20)
labelroll.config(bg="blue",fg="white")

inputroll=Entry(data)
inputroll.grid(row=2,column=100)
inputroll.config(bg="blue",fg="white")

TAM=Label(data,text="TAMIL")
TAM.grid(row=10,column=50,padx=20,pady=20)
TAM.config(bg="blue",fg="white")

inputt=Entry(data)
inputt.grid(row=10,column=100)
inputt.config(bg="blue",fg="white")

ENG=Label(data,text="ENGLISH")
ENG.grid(row=12,column=50,padx=20,pady=20)
ENG.config(bg="blue",fg="white")

inputE=Entry(data)
inputE.grid(row=12,column=100)
inputE.config(bg="blue",fg="white")

MATH=Label(data,text="MATHS")
MATH.grid(row=14,column=50,padx=20,pady=20)
MATH.config(bg="blue",fg="white")

inputM=Entry(data)
inputM.grid(row=14,column=100)
inputM.config(bg="blue",fg="white")

PHY=Label(data,text="PHYSICS")
PHY.grid(row=16,column=50,padx=20,pady=20)
PHY.config(bg="blue",fg="white")

inputP=Entry(data)
inputP.grid(row=16,column=100)
inputP.config(bg="blue",fg="white")

insbut=Button(data,text="INSERT",command=insert)
insbut.grid(row=25,column=20,padx=40,pady=40)
insbut.config(bg="black",fg="white")

insbut=Button(data,text="UPDATE")
insbut.grid(row=25,column=50,padx=40,pady=40)
insbut.config(bg="green",fg="yellow")

insbut=Button(data,text="DELETE")
insbut.grid(row=25,column=80,padx=40,pady=40)
insbut.config(bg="red")

insbut=Button(data,text="RESET")
insbut.grid(row=25,column=150,padx=40,pady=40)
insbut.config(bg="orange")

insbut=Button(data,text="TRUNCATE")
insbut.grid(row=25,column=250,padx=40,pady=40)
insbut.config(bg="dark red")



data.mainloop()






