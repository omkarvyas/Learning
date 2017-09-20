

#import all the modules you need
import turtle


#def set_background():

window = turtle.Screen()
window.bgcolor("blue")    

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed("2")
    sides_of_sqr = 4

    for x in range (0,18):
        brad.setheading(20*x)
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
    angie.circle(100)


def draw_trangle():
    jim = turtle.Turtle()
    jim.color("white")
    jim.setheading(0)
    jim.forward(100)
    jim.setheading(90)
    jim.forward(100)
    jim.home()
    window.exitonclick()
    

draw_square()
draw_circle()
draw_trangle()

    
