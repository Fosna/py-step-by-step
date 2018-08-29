from turtle import *
from random import randint

colors = ['red', 'blue', 'orange', 'purple', 'violet', 'tomato'];

turtles = []

turtle_y = 100

for color in colors:
    single_turtle = Turtle()
    single_turtle.color(color)
    single_turtle.shape('turtle')
    single_turtle.penup()
    single_turtle.goto(-160, turtle_y)
    turtle_y -= 30
    single_turtle.pendown()
    turtles.append(single_turtle)

# ant = Turtle()
# ant.color('red')
# ant.shape('turtle')
# ant.penup()
# ant.goto(-160, 100)
# ant.pendown()

# for chunk in range(12):
#     ant.right(30)

# bee = Turtle()
# bee.color('blue')
# bee.shape('turtle')
# bee.penup()
# bee.goto(-160, 70)
# bee.pendown()


speed(10)
penup()
goto(-140, 140)

for step in range(14):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(210)
    penup()
    backward(220)
    left(90)
    forward(20)

for turn in range(100):
    for tu in turtles:
        tu.forward(randint(1, 5))

exitonclick()
done()
