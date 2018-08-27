from turtle import *

my_rect_x = 0

def init(): 
    screen = Screen()
    width = 300
    height = 300
    screen.setup(width, height)
    bgcolor('pink')

    showturtle()
    speed(0)

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

def my_rect():
    global my_rect_x

    my_rect_x += 10

    clear()
    stroke_rect(my_rect_x, 10, 20, 40)
    
    ontimer(my_rect, 500)

def main():

    
    ontimer(my_rect, 3000)

    exitonclick()


init()
main()
