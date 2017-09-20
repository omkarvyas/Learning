#import all the modules you need
import turtle #To Use grapichs class Turtle
import signal #To catch signals#
import sys    #To System exit 



window = turtle.Screen()
window.bgcolor("white")    

def draw_fractal():
    x = turtle.Turtle()
    #fractal(x,300,1,0)
    koch(x,5,300)
    window.exitonclick()

    

def fractal(one_turtle,length,ori,recur):
    recur = recur+1
    tt = one_turtle
    tt.speed('slowest')

    for i in range(1,4):
        if(recur<4):
            print("recur = ",recur)
            print("ori = ",ori)
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


       
try:
    draw_fractal()
    

except KeyboardInterrupt:
    print "Bye"
    window.exitonclick()
    sys.exit()
    


    
