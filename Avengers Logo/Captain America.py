#Captain America

from turtle import *

setup(width = 1.0, height = 1.0 ,startx = None, starty = None)
speed(0.1)
# background color
bgcolor('#00599c')
pensize(1)

#1 Outer red circle

penup()
goto(0,-120)
pendown()

pencolor('red')
fillcolor('red')
begin_fill()
circle(180)
end_fill()

#2 Outer white circle

penup()
goto(0,-80)
pendown()

pencolor('white')
fillcolor('white')
begin_fill()
circle(140)
end_fill()

#3 Inner red circle
penup()
goto(0,-40)
pendown()

pencolor('red')
fillcolor('red')
begin_fill()
circle(100)
end_fill()

#4 Inner blue circle
penup()
goto(0,0)
pendown()

pencolor('blue')
fillcolor('blue')
begin_fill()
circle(60)
end_fill()

# Outer Star

penup()
goto(-54,77)
pendown()

pencolor('white')
fillcolor('white')
begin_fill()
for i in range(5):
    forward(107)
    right(144)
end_fill()

# Inner Star

penup()
goto(-30,70)
pendown()


pencolor('grey')

for i in range(5):
    forward(60)
    right(144)
end_fill()

penup()
goto(0,49)
pendown()

pencolor('white')
fillcolor('white')
begin_fill()
circle(12)
end_fill()

hideturtle()    # removes the turtle icon

done()


##################################################







