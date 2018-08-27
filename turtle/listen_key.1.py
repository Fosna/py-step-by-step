from turtle import *

cat_x = 0
cat_y = 0
refresh_interval_ms = 100

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
    clear()
    goto(cat_x, cat_y)
    stamp()

    ontimer(my_timer, refresh_interval_ms)


def up():
    global cat_y
    cat_y += 5


def down():
    global cat_y
    cat_y -= 5


def left():
    global cat_x
    cat_x -= 5


def right():
    global cat_x
    cat_x += 5


def main():
    screen = Screen()

    screen.onkey(up, 'Up')
    screen.onkey(down, 'Down')
    screen.onkey(left, 'Left')
    screen.onkey(right, 'Right')

    cat_grumpy = 'cat_grumpy.gif'
    addshape(cat_grumpy)
    
    shape(cat_grumpy)
    ontimer(my_timer, refresh_interval_ms)

    screen.listen()
    done()


init()
main()
