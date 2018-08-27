from turtle import *

def init(): 
    screen = Screen()
    width = 300
    height = 300
    screen.setup(width, height)
    bgcolor('pink')

    showturtle()
    speed(1)

def fill_rect(w, h):
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
    fill_rect(20, 20)

    end_fill()

    exitonclick()

init()
main()
