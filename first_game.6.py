from turtle import *
from random import randint

bug_x = 0
bug_y = -100
bug_w = 80
bug_h = 48
bug_speed = 10
bug_img = 'ladybug.gif' 

melon_x = 0
melon_y = 150
melon_w = 43
melon_h = 30
melon_speed = 10
melon_img = 'watermelon2.gif'

score = 0

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

def images_touching(x1, y1, w1, h1, x2, y2, w2, h2):
    if (x1 >= x2 + w2 or x1 + w1 <= x2 ):
        return False
    if (y1 > y2 + h2 or y1 + h1 <= y2):
        return False
    return True

def do_a_frame():
    global bug_x
    global melon_y
    global melon_x
    global score
    
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

    if (images_touching(bug_x, bug_y, bug_w, bug_h, melon_x, melon_y, melon_w, melon_h)):
        score += 1
        # move off the screen to avoid score going upa lot
        melon_x = -200

    goto(-120, 120)
    pendown()
    print(score)
    write('Score: ' + str(score))
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
