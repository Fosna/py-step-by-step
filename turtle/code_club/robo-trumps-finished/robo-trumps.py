from turtle import *
from random import choice
import os

def get_abs_path(rel_path):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), rel_path))

screen = Screen()
screen.bgcolor('white')
penup()
hideturtle()
robots = {}

file = open(get_abs_path('cards.txt'), 'r')

for line in file.read().splitlines():
  name, battery, intelligence, usefulness, speed, image, colour = line.split(', ')
  image = get_abs_path(image)
  robots[name] = [battery, intelligence, usefulness, speed, image, colour]
  screen.register_shape(image)
file.close()

print('Robots: ', ', '.join(robots.keys()), ' (or random)')

while True:
  robot = input("Choose a robot: ")
  if(robot == "random"):
    robot = choice(list(robots.keys()))
    print(robot)

  if robot in robots:
    stats = robots[robot]
    style = ('Courier', 14, 'bold')
    clear()
    color(stats[5])
    goto(0, 100)
    shape(stats[4])
    setheading(90)
    stamp()
    setheading(-90)
    forward(60)
    write('Name: ' + robot, font=style, align='center')
    forward(25)
    write('Battery: ' + stats[0], font=style, align='center')
    forward(25)
    write('Intelligence: ' + stats[1], font=style, align='center')
    forward(25)
    write('Usefulness: ' + stats[2], font=style, align='center')
    forward(25)
    write('Speed: ' + stats[3], font=style, align='center')

  else:
    print("Robot doesn't exist!")

done()
