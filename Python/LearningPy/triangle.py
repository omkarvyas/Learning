import turtle
import signal
import sys

window = turtle.Screen()
window.bgcolor("white")


def draw_triangle_up(x, length):
    some_t = x
    for i in range(1, 4):
        some_t.fd(length)
        some_t.left(120)


def fractal():
    # type: () -> object
    brad = turtle.Turtle()
    for i in range(1, 3):
        for j in range(1, 3):
            for l in range(1, 4):
                for m in range(1, 5):
                    draw_triangle_up(brad, 50)
                    brad.fd(50)
                brad.left(120)
            brad.fd(200)
        brad.left(120)

    window.exitonclick()


fractal()
# draw_triangle()
