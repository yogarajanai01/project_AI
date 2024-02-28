from tkinter import *

car=Tk()

car.title("TATA CARS DETAILS")
car.geometry("500x500+500+100")
car.state("zoomed")
car.config(bg="blue")

def details(): 
    tb1=(tbentry1.get())
    labelouptut.config(text="Details of"+" "+tb1+" "+"cars is given.")

def info():
    tb2=(tbentry2.get())
    labelouptut2.config(text="tata"+" "+tb2+" "+"are safe and secure.")

labeltitle=Label(car,text="brand name",bg="white")
labeltitle.grid(row=0,column=20,padx=200,pady=30)

tbentry1=Entry(car,width=50)
tbentry1.grid(row=0,column=30)

labeltitle2=Label(car,text="car name",bg="white")
labeltitle2.grid(row=1,column=20,padx=200,pady=30)

tbentry2=Entry(car,width=50)
tbentry2.grid(row=1,column=30)

labelouptut=Label(car,text="",bg="white")
labelouptut.grid(row=3,column=30, pady=20)

labelouptut2=Label(car,text="",bg="white")
labelouptut2.grid(row=3,column=90, pady=20)

btnAdd=Button(car,text="details", command=details)
btnAdd.grid(row=4, column=20)

btnAdd=Button(car,text="info", command=info)
btnAdd.grid(row=4, column=50)

car.mainloop()


