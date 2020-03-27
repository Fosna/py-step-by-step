from turtle import *

def init(): 
    screen = Screen()
    width = 480
    height = 360
    screen.setup(width, height)
    bgcolor('pink')

    showturtle()
    speed(1)

def stroke_rect(w, h):
    for i in range(2):
        fd(w)
        rt(90)
        fd(h)
        rt(90)

def main():
    penup()
    goto(10, 10)
    pendown()

    begin_fill()
    stroke_rect(20, 20)

    end_fill()

    exitonclick()

init()
main()
