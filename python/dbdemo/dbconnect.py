import mysql.connector
from tkinter import *

class dataManipulate:
    def __init__(self):
     print("Welcome to db manipulation")

    def returnmsg(self):
        return "connected"
    
    def mydbconnection(self):
        con=mysql.connector.connect(
            host="192.168.1.240",
            user="AIBATCH01",
            password="AI@123",
            databse="ai_yogarajan"
        )
        return con
    
    def insertvalues(self,NAME,TAMIL,ENGLISH,MATHS,PHYSICS):
       student_name=NAME
       st_mk_tamil=TAMIL
       st_mk_english=ENGLISH
       st_mk_maths=MATHS
       st_mk_physics=PHYSICS

       data=self.mydbconnection()
       result=data.cursor()

       stmts="Insert into STD_MARKS (NAME,TAMIL,ENGLISH,MATHS,PHYSICS) VALUES ("+ '"' +student_name + '"' + "," + str(st_mk_tamil) + "," + str(st_mk_english) + "," +str(st_mk_maths) + "," + str(st_mk_physics) + ");"

       result.execute(stmts)
       print(stmts)


       data.commit()

       return (str(result.rowcount) + "row inserted")