from turtle import *
# background color
bgcolor('black')

speed(0.1)

# Logo

penup()         #
forward(-70)    #
right(90)       #
forward(90)     # adjusting the position
left(90)        #
pendown()       #

pensize(1)
pencolor('red')
fillcolor('red')
begin_fill()
for i in range(2):
    forward(150)
    left(120)
    forward(100)
    right(60)
    forward(100)
    left(120)
end_fill()

ht()
done()

