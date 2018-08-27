from turtle import *
from random import randint

bug_x = 0
bug_y = -100
bug_speed = 10
bug_img = 'ladybug.gif' 

melon_x = 0
melon_y = 150
melon_speed = 10
melon_img = 'watermelon2.gif'

frame_interval_ms = 100
screen = None



def init(): 
    global screen

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

def images_touching(x1, y1, w1, h1, x2, y2, w2, h2)
    if (x1 >= x2 + w2 or x1 + w1 <= x2 ):
        return False
    if (y1 > y2 + h2 or y1 + h1 <= y2):
        return False
    return True

def do_a_frame():
    global melon_y
    global melon_x
    
    clear()
    
    shape(bug_img)
    goto(bug_x, bug_y)
    stamp()

    shape(melon_img)
    melon_y -= melon_speed
    # reset melon
    if (melon_y < -150):
        melon_y = 150
        melon_x = randint(-150, 150)

    goto(melon_x, melon_y)
    stamp()

    goto(-120, 120)
    pendown()
    write('Score: 0')
    penup()

    ontimer(do_a_frame, frame_interval_ms)


def left():
    global bug_x

    if (-150 < bug_x - bug_speed):
        bug_x -= bug_speed
    

def right():
    global bug_x

    if (bug_x + bug_speed < 150):
        bug_x += bug_speed


def main(): 
    addshape(bug_img)
    addshape(melon_img)
    penup()

    screen.onkey(left, 'Left')
    screen.onkey(right, 'Right')

    ontimer(do_a_frame, frame_interval_ms)

    screen.listen()
    done()


init()
main()
