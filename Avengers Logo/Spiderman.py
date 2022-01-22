# My Spider Code

from turtle import *

speed(0.1)

# background color
bgcolor('red')

pensize(0.1)
pencolor('black')
# For circle head

fillcolor('black')
begin_fill()
circle(23)  
end_fill()
  
# For hexagon body

penup()        #
right(90)      # 
forward(0)     # adjusting position
pendown()      #
goto(0,22)     #

fillcolor('black')
begin_fill()
right(60)
for i in range(6):   
    forward(50)
    left(60)
end_fill()
penup()

# For legs 

pensize(1)

#1 Inner right leg

left(150)      #
forward(34)    #
goto(30,10)    # adjusting position
left(90)       #
forward(9)     #
pendown()      #

begin_fill()
forward(25) 
right(60)
forward(15)
left(60)
forward(25)
right(30)
forward(21)     
right(150)
forward(50)
right(60)
forward(15)    
left(60)
forward(15)
left(60)
forward(35)
right(60)
forward(100)
right(150)
forward(21) 
right(30)
forward(77) 
left(60)
forward(35)
end_fill()

#2 Outer right leg

penup()            #
right(150)         #
forward(55)        #
right(90)          # adjusting position
forward(100)       #
left(180)          #
pendown()          #

begin_fill()
forward(90)
left(60)
forward(40)
right(60)
forward(5)
right(60)
forward(20)
left(60)
forward(55)
right(30)
forward(21)
right(150)
forward(80)
right(70)
forward(15)
left(135)
forward(35)
right(65)
forward(130)
right(150)
forward(21)
right(30)
forward(20)
end_fill()

#3 Inner left leg

penup()           #
goto(-30,20)      # adjusting the position 
pendown()         #  

begin_fill()
forward(25) 
left(60)
forward(15)
right(60)
forward(25)
left(30)
forward(21)     
left(150)
forward(50)
left(60)
forward(15)    
right(60)
forward(15)
right(60)
forward(35)
left(60)
forward(100)
left(150)
forward(21) 
left(30)
forward(77) 
right(60)
forward(35)
end_fill()



#4 Outer left leg

penup()           #
left(60)          # adjusting the position
goto(-82,-82)     # 
pendown()         #

begin_fill()                                                                                                        
forward(90)
right(60)                                                                                                      
forward(40)
left(60)                                                                               
forward(5)
left(60)
forward(20)                         
right(60)                                                                                       
forward(55)                                                                           
left(30)                             
forward(21)                                                                              
left(150)                                                                                
forward(80)                                                                                                     
left(70)                                                       
forward(15)
right(135)                                                                                                               
forward(35)                                                                                                  
left(65)                                                                           
forward(130)                                                                                                                           
left(150)
forward(21)
left(30)                                                                                                                  
forward(20)
end_fill()

hideturtle()    # removes the turtle icon 


done()





##############################################################################################################



