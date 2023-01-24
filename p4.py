import turtle
from  turtle import *
s=turtle.Screen()
s.bgcolor("green")
color('red')
begin_fill()
left(50)
forward(100)
circle(40,180)
left(260)
circle(40,180)
forward(100)

end_fill()
turtle.penup()
turtle.goto(-105,-150)
turtle.pendown()
turtle.color('white')
turtle.write("I LOVE YOU",font=("Verdana",25,'bold'))

turtle.penup()
turtle.goto(-70,-50)
turtle.pendown()
turtle.color('white')
turtle.write("RAMYA   SHREE",font=("Verdana",30,"bold"))

done()
