from turtle import *

setup(500,650)
title("And I am IRONMAN..!")
hideturtle()

speed(0.1)  #speed of turtle  ,Giving values > 1 slows the tutle

bgcolor('#304c8a')

#Top red

pensize(0.1)
color('#b70006')   #red

penup()
goto(-60,-140)
pendown()

begin_fill()
forward(140*1.2)
left(60)
forward(100*1.2)
right(20)
forward(30*1.2)
left(50)
forward(210*1)
left(30)
forward(70*1.2)
left(23)

circle(180*1.4,74)

left(23)
forward(70*1.2)
left(30)
forward(210*1)
left(50)
forward(30*1.2)
right(20)
forward(100*1.2)
left(60)

end_fill()

#Bottom red
penup()
goto(-90,-280)
pendown()

begin_fill()
fd(180)
lt(45)
fd(60)
lt(30)
fd(200)
lt(105)
fd(367)
lt(105)
fd(200)
lt(30)
fd(60)
end_fill()


penup()
goto(-150,20)
lt(45)
pendown()


#eye color

color("#67cadc")   # light blue
begin_fill()
for  j in range(2):
    fd(300)
    rt(90)
    fd(90)
    rt(90)
end_fill()



# Top yellow Part
piece1=[[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10), (-40, -20), (0, -20)],[(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260), (40, 120), (0, 120)]]
# Middle yellow Part
piece2=[[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210), (-80, -230), (-64, -210), (0, -210)],[(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]]
# Bottom yellow Part
piece3=[[(-60, -220), (-80, -240), (-110, -220), (-120, -250),(-90, -280), (-60, -260), (-30, -260), (-20, -250), (0, -250)],[(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250),(110, -220), (80, -240), (60, -220), (0, -220)]]




piece1Goto=(0,120)
piece2Goto=(0,-30)
piece3Goto=(0,-220)

def draw_piece(piece,pieceGoto):
    penup()
    goto(pieceGoto)
    pendown()
    pencolor("black")
    fillcolor('#fab104') #Light Yellow 
    begin_fill()
    for i in range(len(piece[0])):
        x,y=piece[0][i]
        goto(x,y)
    
    for i in range(len(piece[1])):
        x,y=piece[1][i]
        goto(x,y)
    end_fill()
draw_piece(piece1,piece1Goto)
draw_piece(piece2,piece2Goto)
draw_piece(piece3,piece3Goto)

#Tiny adjustments
penup()
goto(-40,-20)
pendown()
color("#fab104")
begin_fill()
for  j in range(1):
    pencolor("#fab104")
    fd(80)
    rt(90)
    pencolor("black")
    fd(5)
    rt(90)
    fd(80)
    rt(90)
    pencolor("black")
    fd(5)
end_fill()

penup()
goto(-40,-30)
pendown()


hideturtle()

done()

