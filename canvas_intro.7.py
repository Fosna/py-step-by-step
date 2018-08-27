from turtle import *

def init(): 
    screen = Screen()
    width = 300
    height = 300
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


def main():
    color('black')
    write('Hello', font=('Arial', 60, 'normal'))

    exitonclick()

init()
main()
