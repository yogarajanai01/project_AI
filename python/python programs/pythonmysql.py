import mysql.connector
con = mysql.connector.connect(
    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_yogarajan"
)
print(con)
result=con.cursor()
#result.execute("show tables")
#resultshow=result.fetchall()
#for x in resultshow:
 #   print(x)
#result.execute("select * from kabaddi_players")
#resultshow=result.fetchall()
#for x in resultshow:
 #   print(x)    
 
