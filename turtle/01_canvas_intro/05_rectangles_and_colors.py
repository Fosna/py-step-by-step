from turtle import *

def init(): 
    screen = Screen()
    width = 480
    height = 360
    screen.setup(width, height)
    bgcolor('pink')

    showturtle()
    speed(5)

def fill_rect(x, y, w, h):
    penup()
    goto(x, y)
    pendown()
        
    begin_fill()
    for i in range(2):
        fd(w)
        rt(90)
        fd(h)
        rt(90)

    end_fill()

def main():
    fill_rect(10, 10, 20, 20)

    color('red', 'red')
    fill_rect(50, 50, 20, 40)
    fill_rect(80, 50, 20, 40)

    color('green', 'green')
    fill_rect(30, 110, 90, 20)
    fill_rect(30, 150, 90, 20)

    exitonclick()

init()
main()
