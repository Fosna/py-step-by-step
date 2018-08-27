from turtle import *

def clicked(x, y):
    print(x)
    print(y)
    print('clicked')

screen = Screen()
screen.setup(480, 360)
speed(0)

bgpic('./pic/bg.gif')

drum_hit = './pic/hit.gif'
addshape(drum_hit)

pu()
goto(178, -100)
shape(drum_hit)
stamp()


hideturtle()

screen.onclick(clicked)

done()
