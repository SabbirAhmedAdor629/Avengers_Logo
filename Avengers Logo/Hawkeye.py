#Hawkeye Logo
from turtle import *

bgcolor('black')
speed(0.1)

#Outer circle
goto(0,-180)
pensize(35)
color("#4B0082")
circle(200)


pensize(1)

#Symbol
penup()
goto(0,50)
pendown()

begin_fill()
lt(30)
fd(130)
rt(120)
fd(170)
rt(60)
fd(130)
rt(60)
fd(130)
rt(60)
fd(170)
rt(120)
fd(130)
end_fill()

ht()
