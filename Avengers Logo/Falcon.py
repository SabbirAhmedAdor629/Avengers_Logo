#New falcon
from turtle import *
speed(0.11)

setup(width = 1.0, height = 1.0 ,startx = None, starty = None)

bgcolor("#4527a0")
color("silver")
pencolor("black")
pensize(3)

#Outer grey circle

penup()
goto(0,-90)
pendown()

begin_fill()
circle(180)
end_fill()

#Inner circle

penup()
goto(0,-60)
pendown()

pensize(20)
begin_fill()
circle(150)
end_fill()

#Outer red wing

color("red")
pencolor("black")
pensize(10)

penup()
goto(0,-25)
pendown()

begin_fill()
goto(15,30)
goto(150,70)
lt(82.5)
circle(150,61)
goto(0,160)
goto(-90,210)
lt(73)
circle(150,61)
goto(-15,30)
goto(0,-25)
end_fill()

#Arrow Design

pensize(10)
goto(65,195)
penup()
goto(0,-25)
pendown()
goto(-65,195)

#Left wing lines
pensize(4)
penup()
goto(30,70)
pendown()
goto(147,117)
penup()
goto(42,118)
pendown()
goto(130,165)

#Right wing lines

penup()
goto(-30,70)
pendown()
goto(-145,117)
penup()
goto(-42,118)
pendown()
goto(-130,165)

ht()

