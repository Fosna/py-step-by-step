from turtle import *

bug_x = 0
bug_y = -100
bug_speed = 10
bug_img = 'ladybug.gif' 
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

def do_a_frame():
    clear()
    
    goto(bug_x, bug_y)
    stamp()

    print(position())

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
    shape(bug_img)
    penup()

    screen.onkey(left, 'Left')
    screen.onkey(right, 'Right')

    ontimer(do_a_frame, frame_interval_ms)

    screen.listen()
    done()


init()
main()
