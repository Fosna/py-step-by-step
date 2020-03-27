from turtle import *

def init(): 
    screen = Screen()
    width = 480
    height = 360
    screen.setup(width, height)
    bgcolor('pink')

    showturtle()
    speed(5)

def fill_rect(x, y, w, h):
    begin_fill()
    stroke_rect(x, y, w, h)
    end_fill()


def stroke_rect(x, y, w, h):
    penup()
    goto(x, y)
    pendown()
    
    for i in range(2):
        fd(w)
        rt(90)
        fd(h)
        rt(90)

def circle_from_center(r):
    (x, y) = position()

    penup()
    goto(x, y - r)
    pendown()

    circle(r)

    penup()
    goto(x, y)
    pendown()


def main():
    color('green', 'green')
    begin_fill()
    circle_from_center(25)
    end_fill()

    color('red', 'red')
    circle_from_center(50)

    exitonclick()


init()
main()
