# avengers 
from turtle import *


bgcolor('black')
speed(0.1)

# outer white circle
setposition(0,-180)
pensize(7)
pendown()
begin_fill()
fillcolor('#4527a0')  
pencolor('white')
circle(200)       
end_fill()
penup()

#

# inner circle
pensize(2)
setposition(0, -140)
pendown()
begin_fill()
color('black')
circle(160)
end_fill()
penup()

#A
setposition(10, -70) # 30,-110
pendown()
begin_fill()
color('#4527a0')   #violet  #4527a0    #4B0082  
pensize(10)
pencolor('#a62c2b')  #metallic red  #a62c2b 
forward(23*0.7)
backward(123*0.7)
left(60)
backward(220*0.7)
right(60)
backward(100*0.7)
right(117)
backward(710*0.7)
right(63)
backward(110*0.7)
right(90)
backward(510*0.7)
right(90)
backward(100*0.7)
right(90)
backward(70*0.7)
end_fill()
penup()

# Inner triangle of A
penup()
setposition(27, -20) # 53,-40
pendown()
begin_fill()
color('black')
pencolor('#a62c2b')   #metallic red #a62c2b

right(90)
forward(100*0.7)
right(115)
forward(250*0.7)
right(155) 
forward(227*0.7)
end_fill()

#arrow

backward(40)
left(42)
forward(140*0.6) 
right(83)
forward(140*0.66)

#Additional extra lines

penup()
lt(10)
goto(-54,-75)
pensize(3)
color("white")
pendown()
forward(153)

penup()
lt(5)
goto(23,110)
pensize(3)
color("white")
pendown()
forward(135)

penup()
rt(64)
goto(20,-75)
pensize(3)
color("white")
pendown()
forward(75)

penup()
goto(-135,-208)
pensize(3)
color("white")
pendown()
forward(75)


#Outer cut red ring

penup()
goto(0,225)
pendown()
pensize(8)
pencolor("#a62c2b")    #metallic red #a62c2b
circle(205,126)
penup()
circle(205,27)
pendown()
circle(205,175)


#Text

penup()
goto(-150,-300)
pendown()
color("#a62c2b")
write("A",font = ("Helvetica",80,"bold italic")) #Courier, Times ,Comic Sans MS
penup()
goto(-80,-290)
pendown()
color("#a62c2b")
write("VENGERS",font = ("Helvetica",40,"bold italic"))

#Text shadow

penup()
goto(-152,-298)
pendown()
color("#4527a0")
write("A",font = ("Helvetica",80,"bold italic")) #Courier, Times ,Comic Sans MS
penup()
goto(-82,-288)
pendown()
color("#4527a0")
write("VENGERS",font = ("Helvetica",40,"bold italic"))




ht()
