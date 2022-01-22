#Captain America's Shield

from turtle import *

speed(0.1)
# background color
bgcolor('#00599c')
pensize(1)

#1 Outer red circle
pencolor('red')
fillcolor('red')
begin_fill()
circle(100)
end_fill()

#2 Outer white circle

penup()
goto(0,20)
pendown()

pencolor('white')
fillcolor('white')
begin_fill()
circle(80)
end_fill()

#3 Inner red circle
penup()
goto(0,40)
pendown()

pencolor('red')
fillcolor('red')
begin_fill()
circle(60)
end_fill()

#4 Inner blue circle
penup()
goto(0,60)
pendown()

pencolor('blue')
fillcolor('blue')
begin_fill()
circle(40)
end_fill()

# Outer Star

penup()
goto(-36,111)
pendown()

pencolor('white')
fillcolor('white')
begin_fill()
for i in range(5):
    forward(72)
    right(144)
end_fill()

# Inner Star

penup()
goto(-20,107)
pendown()


pencolor('grey')

for i in range(5):
    forward(40)
    right(144)
end_fill()

penup()
goto(0,93)
pendown()

pencolor('white')
fillcolor('white')
begin_fill()
circle(7.5)
end_fill()

hideturtle()    # removes the turtle icon

done()


##################################################






