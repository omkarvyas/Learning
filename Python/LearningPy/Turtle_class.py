#import all the modules you need
import turtle
import signal
import sys
import random

colors  = ["red","green","blue","orange","purple","pink","yellow"] # Make a list of colors to picvk from
""" Window Paramaeters where you want to draw"""

window = turtle.Screen()
window.bgcolor("white")    


"""draw_square_which_makes_circle method"""
def draw_square_which_makes_circle():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed("2")
    sides_of_sqr = 4

    for x in range (0,36):
        brad.setheading(10*x)
        sides_of_sqr = 4
        while(sides_of_sqr):
            brad.forward(100)
            brad.right(90)
            sides_of_sqr = sides_of_sqr - 1;
        print "square : %d" %(x)


"""Draw Dandelian kind of flower"""
def draw_flower():
    o = turtle.Turtle()
    o.speed(0)
       
    for i in range (1,73):
        color = random.choice(colors) #Choose a random color
        o.color(color)
        draw_rhombus(o)
        o.right(5)
    o.pensize(6)
    o.color("green")
    o.right(-270)
    o.forward(400)
    o.pensize(3)
    o.right(110)
    draw_rhombus(o)


    
def draw_rhombus(some_turtle):
    for i in range(1,3):
        some_turtle.forward(100)
        some_turtle.right(30)
        some_turtle.forward(100)
        some_turtle.right(150)

def draw_trangle_down(t_turtle, fwd_len):
    t_turtle.forward(fwd_len)
    t_turtle.right(120)
    t_turtle.forward(fwd_len)
    t_turtle.right(120)
    t_turtle.forward(fwd_len)

def draw_trangle_up(t_turtle, fwd_len):
    t_turtle.forward(fwd_len)
    t_turtle.right(-120)
    t_turtle.forward(fwd_len)
    t_turtle.right(-120)
    t_turtle.forward(fwd_len)


def draw_try():
    x = turtle.Turtle()
    fractal(x,200,1,0)
#    draw_trangle_up(x,250)
#    x.home()
#    draw_trangle_down(x,100)
    

def fractal(one_turtle,length,ori,recur):
    recur = recur+1
    tt = one_turtle

    for i in range(1,4):
        if(recur<4):
            tt.forward(length/2)
            tt.left(120)
            fractal(tt,length/2,0,recur)
            tt.right(120)
            tt.forward(length/2)
        else:
            tt.forward(length)
        if(ori==1):
            tt.left(120)
        else:
            tt.right(120)


            

try:
    #draw_square_which_makes_circle()
    draw_flower()
    #draw_try()
    window.exitonclick()
except KeyboardInterrupt:
    print "Bye"
    window.exitonclick()
    sys.exit()
    


    
