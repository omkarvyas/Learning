

#import all the modules you need
import turtle
import signal
import sys



#def set_background():

window = turtle.Screen()
window.bgcolor("blue")    

def draw_square():
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


def draw_circle():    
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("red")
    for i in range(1,73):
        draw_rhombus(angie)
        angie.right(5)


    
    #angie.circle(100)
    #angie.stamp()
    #angie.penup()


def draw_trangle():
##    jim = turtle.Turtle()
##    jim.color("white")
##    jim.setx(200)
##    jim.sety(200)
##    jim.setheading(0)
##    jim.forward(100)
##    jim.setheading(90)
##    jim.forward(100)
    #jim.home()
    window.exitonclick()

def draw_name():
    o = turtle.Turtle()
    o.color("red")
    o.setpos(-300,-300)
    for i in range (1,73):
        draw_rhombus(o)
        o.right(5)
    
    #o.fill(True)
    #o.begin_fill()
    #o.circle(120,180)
    #o.end_fill()
    
def draw_rhombus(some_turtle):
    for i in range(1,3):
        some_turtle.forward(50)
        some_turtle.right(30)
        some_turtle.forward(50)
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


        
    

            
    
    #draw_rhombus(x)
    #draw_circle()
    #x.right(270)
    #x.forward(100)
       
        



#draw_square()
#draw_circle()
#draw_name()
try:
    draw_try()
    draw_trangle()
except KeyboardInterrupt:
    print "Bye"
    window.exitonclick()
    sys.exit()
    


    
