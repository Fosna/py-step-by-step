from turtle import *

def init(): 
    screen = Screen()
    width = 480
    height = 360
    screen.setup(width, height)
    bgcolor('pink')

    showturtle()
    speed(1)

def main():
    penup()
    goto(10, 10)
    pendown()

    begin_fill()
    for i in range(4):
        fd(20)
        rt(90)

    end_fill()

    exitonclick()

init()
main()
