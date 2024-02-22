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

    outmsg.config(text="row inserted")

def updatename():
    valuename=str(inputName.get())
    Sno=int(inputsno.get())
    e_con=Mydbconnection()
    result=e_con.cursor()

    statement="update STD_MARKS set Name = (%s) where SNO =(%s);"
    valuepass=(valuename,Sno)
    result.execute(statement,valuepass)
    e_con.commit()

    outmsg.config(text="Name updated")

def updateroll():
    valueRoll=int(inputroll.get())
    Sno=int(inputsno.get())
    e_con=Mydbconnection()
    result=e_con.cursor()

    statement="update STD_MARKS set Roll_No = (%s) where SNO =(%s);"
    valuepass=(valueRoll,Sno)
    result.execute(statement,valuepass)
    e_con.commit()

    outmsg.config(text="Roll updated")

def updateTAMIL():
    valueRoll=int(inputt.get())
    Sno=int(inputsno.get())
    e_con=Mydbconnection()
    result=e_con.cursor()

    statement="update STD_MARKS set TAMIL = (%s) where SNO =(%s);"
    valuepass=(valueRoll,Sno)
    result.execute(statement,valuepass)
    e_con.commit()

    outmsg.config(text="Tamil mark updated")
def updateEng():
    valueRoll=int(inputE.get())
    Sno=int(inputsno.get())
    e_con=Mydbconnection()
    result=e_con.cursor()

    statement="update STD_MARKS set ENGLISH = (%s) where SNO =(%s);"
    valuepass=(valueRoll,Sno)
    result.execute(statement,valuepass)
    e_con.commit()

    outmsg.config(text="English mark updated")
    
def updateMath():
    valueRoll=int(inputM.get())
    Sno=int(inputsno.get())
    e_con=Mydbconnection()
    result=e_con.cursor()

    statement="update STD_MARKS set MATHS = (%s) where SNO =(%s);"
    valuepass=(valueRoll,Sno)
    result.execute(statement,valuepass)
    e_con.commit()

    outmsg.config(text="Maths mark updated")

def updatePhy():
    valueRoll=int(inputP.get())
    Sno=int(inputsno.get())
    e_con=Mydbconnection()
    result=e_con.cursor()

    statement="update STD_MARKS set PHYSICS = (%s) where SNO =(%s);"
    valuepass=(valueRoll,Sno)
    result.execute(statement,valuepass)
    e_con.commit()

    outmsg.config(text="Physics mark updated")
def delete():
    SNO=int(inputsno.get())
    e_con=Mydbconnection()
    result=e_con.cursor()

    statement="Delete from STD_MARKS where SNO=(%s);"
    valuepass=(SNO,)
    result.execute(statement,valuepass)
    e_con.commit()

    outmsg.config(text="deleted")

labelname=Label(data,text="NAME")
labelname.grid(row=0,column=100,padx=20,pady=20)
labelname.config(bg="blue",fg="white")

inputName=Entry(data)
inputName.grid(row=0,column=200)
inputName.config(bg="blue",fg="white")

labelroll=Label(data,text="ROLL_NO")
labelroll.grid(row=2,column=100,padx=20,pady=20)
labelroll.config(bg="blue",fg="white")

inputroll=Entry(data)
inputroll.grid(row=2,column=200)
inputroll.config(bg="blue",fg="white")

TAM=Label(data,text="TAMIL")
TAM.grid(row=10,column=100,padx=20,pady=20)
TAM.config(bg="blue",fg="white")

inputt=Entry(data)
inputt.grid(row=10,column=200)
inputt.config(bg="blue",fg="white")

ENG=Label(data,text="ENGLISH")
ENG.grid(row=12,column=100,padx=20,pady=20)
ENG.config(bg="blue",fg="white")

inputE=Entry(data)
inputE.grid(row=12,column=200)
inputE.config(bg="blue",fg="white")

MATH=Label(data,text="MATHS")
MATH.grid(row=14,column=100,padx=20,pady=20)
MATH.config(bg="blue",fg="white")

inputM=Entry(data)
inputM.grid(row=14,column=200)
inputM.config(bg="blue",fg="white")

PHY=Label(data,text="PHYSICS")
PHY.grid(row=16,column=100,padx=20,pady=20)
PHY.config(bg="blue",fg="white")

inputP=Entry(data)
inputP.grid(row=16,column=200)
inputP.config(bg="blue",fg="white")

insbut=Button(data,text="INSERT",command=insert)
insbut.grid(row=25,column=100,padx=40,pady=40)
insbut.config(bg="black",fg="white")

insbut=Button(data,text="UPDATENAME",command=updatename)
insbut.grid(row=25,column=200,padx=40,pady=10)
insbut.config(bg="green",fg="yellow")

insbut=Button(data,text="UPDATEROLLNO",command=updateroll)
insbut.grid(row=26,column=200,pady=10)
insbut.config(bg="green",fg="yellow")

insbut=Button(data,text="UPDATETAMIL",command=updateTAMIL)
insbut.grid(row=27,column=200,pady=10)
insbut.config(bg="green",fg="yellow")

insbut=Button(data,text="UPDATEENGLISH",command=updateEng)
insbut.grid(row=28,column=200,pady=10)
insbut.config(bg="green",fg="yellow")

insbut=Button(data,text="UPDATEMATHS",command=updateMath)
insbut.grid(row=29,column=200,pady=10)
insbut.config(bg="green",fg="yellow")

insbut=Button(data,text="UPDATEPHYSICS",command=updatePhy)
insbut.grid(row=30,column=200,pady=10)
insbut.config(bg="green",fg="yellow")

insbut=Button(data,text="DELETE",command=delete)
insbut.grid(row=25,column=800,padx=40,pady=40)
insbut.config(bg="red")

lblsno=Label(data,text="SNO",bg="white",fg="black")
lblsno.grid(row=0,column=400)

inputsno=Entry(data,text="",bg="white",fg="black")
inputsno.grid(row=0,column=550)

outmsg=Label(data,text="",bg="black",fg="white")
outmsg.grid(row=2,column=500)

data.mainloop()






