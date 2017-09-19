import turtle

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("blue")

    brad = turtle.Turtle()
    angie = turtle.Turtle()
    jim = turtle.Turtle()
    
    brad.shape("turtle")
    brad.color("green")
    brad.speed("2")
    sides_of_sqr = 4;

    while(sides_of_sqr):
        brad.forward(100)
        brad.right(90)
        sides_of_sqr = sides_of_sqr - 1;
    
    
    angie.shape("arrow")
    angie.color("red")
    angie.circle(100)

    
    jim.color("white")
    #jim.position
    jim.setheading(0)
    jim.forward(100)
    jim.setheading(90)
    jim.forward(100)
    jim.home()
   

    window.exitonclick()
    

draw_shape()
    
    
