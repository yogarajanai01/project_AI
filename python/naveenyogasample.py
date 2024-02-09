'''def tables():
    print("********TABLES**********")
    a = int(input("value for a :"))
    print("value is :",a)
    b = int(input("value for b :"))
    print("value is :",b)
    while b < 21:
       print (a,"x",b,"=",a*b)
       b += 1
   
tables()'''



import turtle as t
pen = t.Turtle()
t.bgcolor('white')
t.delay(8)
pen.color('red')
pen.begin_fill()
pen.left(40)
pen.forward(120)
pen.circle(80, 190)
pen.right(100)
pen.circle(80, 180)
pen.forward(160)
pen.left(90)
pen.forward(50)
pen.setpos(-60, 100)
pen.end_fill()
def txt():
    pen.up()
    pen.setpos(-60, 100)
    pen.color('black')
    pen.write('I Love you', font=("Comic Sans MS", 20))
txt()
pen.end_fill()
t.exitonclick()