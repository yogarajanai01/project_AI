from tkinter import *
import mysql.connector

win=Tk()
win.title("INSERT into MySql DB ")
win.geometry("500x500")
win.state("zoomed")

frameleft=Frame(win,bg="black",width=500,height=500,padx=30,pady=30)
frameleft.pack(side = LEFT)

frameright=Frame(win,bg="black",width=500,height=500)
frameright.pack(side = RIGHT)

lbltitle=Label(frameleft,text="Insert into MySql")
lbltitle.grid(row=0,columnspan=5)
lblname=Label(frameleft,text="Name")
lblname.grid(row=2,column=1,padx=30,pady=30)
lbltamil=Label(frameleft,text="TAMIL")
lbltamil.grid(row=3,column=1,padx=30,pady=30)
win.mainloop()