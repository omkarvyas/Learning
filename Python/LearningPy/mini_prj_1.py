#import all the modules you need
import turtle #To Use grapichs class Turtle
import signal #To catch signals#
import sys    #To System exit
import random


colors  = ["red","green","blue","orange","purple","pink","yellow"] # Make a list of colors to picvk from

window = turtle.Screen()
window.bgcolor("white")    

def draw_fractal():
    x = turtle.Turtle()
    fractal(x,300,1,0)
    #koch(x,5,300)
    #refine_koch(x,3,300)
    #koch_3(x,300)
    t = fab(6)
    print ("fabonacci = ", t)
    window.exitonclick()

    

def fractal(one_turtle,length,ori,recur):
    recur = recur+1
    tt = one_turtle
    tt.speed(0)
    
 

    for i in range(1,4):
        color = random.choice(colors) #Choose a random color
        tt.color("black",color)
        if(recur<4):
            print("recur = ",recur)
            print("ori = ",ori)
            tt.begin_fill()
            tt.forward(length/2)
            tt.left(120)
            fractal(tt,length/2,0,recur)
            tt.right(120)
            tt.forward(length/2)
            tt.end_fill()
        else:
            tt.forward(length)
        if(ori==1):
            tt.left(120)
        else:
            tt.right(120)


def koch(t,order,size):
    """
    make turtle t draw a koch fractal of order and size leave the turtle facing the same direction
    """
    if order == 0: # the vase case is just a stright line
        t.forward(size)
    else:
        koch(t,order-1,size/3) #Go 1/3 of the way
        t.left(60)
        koch(t,order-1,size/3)
        t.right(120)
        koch(t,order-1,size/3)
        t.left(60)
        koch(t,order-1,size/3)


def refine_koch(t,order,size):
    if order ==0:
        t.forward(size)
    else:
        for angle in [60,-120,60,0]:
            refine_koch(t,order-1,size/3)
            t.left(angle)

""" Simply Recurrsion to understand the refine_koch code """

def koch_0(t,size):
    t.forward(size)

def koch_1(t,size):
    for angle in [60,-120,60,0]:
        koch_0(t,size/3)
        t.left(angle)

def koch_2(t,size):
    for angle in [60,-120,60,0]:
        koch_1(t,size/3)
        t.left(angle)
        
def koch_3(t,size):
    for angle in [60,-120,60,0]:
        koch_2(t,size/3)
        t.left(angle)
        
def fab(n):
    if n <= 1:
        return n
    t = fab(n-1)+fab(n-2)
    return t

        

       
try:
    draw_fractal()
    

except KeyboardInterrupt:
    print "Bye"
    window.exitonclick()
    sys.exit()
    


    
