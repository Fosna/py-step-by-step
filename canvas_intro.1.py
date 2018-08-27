from turtle import *

screen = Screen()
width = 300
height = 300
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

main()