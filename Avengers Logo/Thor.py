# Thor's Mjolnir
from turtle import *
speed(0.1)

setup(width = 1.0, height = 1.0 ,startx = None, starty = None)

bgcolor("black")
color("grey")
pencolor("black")
pensize(3)


#Iron part of hammer

penup()
goto(-90,200)
pendown()

begin_fill()
for iron in range(2):
    fd(150)
    rt(45)
    fd(30)
    rt(45)
    fd(80)
    rt(45)
    fd(30)
    rt(45)
    
    
end_fill()

color("black")
pensize(1)

penup()
goto(-75,187)
pendown()


for iron in range(2):
    fd(150*0.8)
    rt(45)
    fd(30*0.8)
    rt(45)
    fd(80*0.8)
    rt(45)
    fd(30*0.8)
    rt(45)
    
#Wooden handle
    
penup()
goto(-33,77)  #-30
pendown()
fd(30)

color('brown')
pencolor("black")
pensize(4)

begin_fill()
for design in range(8):
    penup()
    rt(90)
    fd(25)
    rt(90)
    fd(25)
    rt(135)
    pendown()
    fd(1.414*25)
    rt(135)
    fd(25)
    lt(90)

rt(180)
fd(25)
rt(90)
fd(200)
rt(90)
fd(25)
end_fill()

#Handle tail

penup()
goto(-20,-132)
rt(120)
pendown()

color("grey")
pensize(7)
fd(70)
circle(14,200)
fd(70)

#Thor symbol

penup()
goto(15,115)
lt(10)
pendown()

color("#7edbc7") #lightblue

for symbol in range(3):
    circle(32,180)
    lt(60)
    
#Additionals

pensize(1)
color('grey')
pencolor("black")

penup()
goto(10,200)
lt(90)
pendown()

begin_fill()
for rect1 in range(2):
    fd(50)
    rt(90)
    fd(7)
    rt(90)
end_fill()

penup()
goto(10,72)
pendown()

begin_fill()
for rect2 in range(2):
    fd(50)
    rt(90)
    fd(7)
    rt(90)
end_fill()   

# Handle cap
penup()
#pensize(5)
goto(-4,-130)
pendown()

begin_fill()
for sq in range(2):
    fd(25)   #width
    rt(90)
    fd(30)  #height
    rt(90)
end_fill()

ht()

