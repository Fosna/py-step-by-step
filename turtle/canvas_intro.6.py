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
# ctx.fillStyle= "green";
# ctx.fillRect(60, 80, 70, 20);

# ctx.strokeStyle= "red";
# ctx.strokeRect(50, 50, 20, 40);

    color('green', 'green')
    fill_rect(60, 80, 70, 20)

    # changed y
    color('red', 'black')
    pensize(5)
    stroke_rect(50, 70, 20, 40)

    exitonclick()

init()
main()
