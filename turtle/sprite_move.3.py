from turtle import *
import os

my_y = 0

def init(): 
    screen = Screen()
    width = 300
    height = 300
    screen.setup(width, height)
    bgcolor('pink')

    hideturtle()
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

def my_timer():
    global my_y
    (x, y) = position()

    my_y += 10

    clear()
    goto(x, my_y)
    stamp()
    
    ontimer(my_timer, 500)

def get_abs_path(rel_path):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), rel_path))

def main(): 
    cat_grumpy = get_abs_path('cat_grumpy.gif')
    addshape(cat_grumpy)
    
    shape(cat_grumpy)
    ontimer(my_timer, 500)

    exitonclick()


init()
main()
