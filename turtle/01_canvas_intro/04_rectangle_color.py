from turtle import *

def init(): 
    screen = Screen()
    width = 600
    height = 360
    screen.setup(width, height)
    bgcolor('pink')

    showturtle()
    speed(5)

def fill_rect(x, y, w, h):
    penup()
    goto(x, y)
    pendown()
        
    for i in range(2):
        fd(w)
        rt(90)
        fd(h)
        rt(90)

def main():
    begin_fill()
    fill_rect(10, 10, 20, 20)
    end_fill()

    color('red', 'red')
    begin_fill()
    fill_rect(50, 50, 20, 40)
    end_fill()

    exitonclick()

init()
main()
