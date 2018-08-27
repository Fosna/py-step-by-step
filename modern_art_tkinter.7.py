#!/bin/python3

from tkinter import *
import random
import time
from math import *

def random_rectangle(canvas, width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)


def random_color():
    return '#{:06x}'.format(random.randint(0, 0xFFFFFF))


def random_circle(canvas, width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    circle_width = random.randrange(width / 2)
    x2 = x1 + circle_width
    y2 = y1 + circle_width

    canvas.create_arc(x1, y1, x2, y2, fill=fill_color, outline=fill_color, extent=359)

# TODO: tkinter draw star
def star_pentagon(canvas, center_x, center_y, radius):
    # A regular star pentagon, {5/2}, has five corners
    # {5/2} star
    # 5 - five vertices
    # 2 - connect every second vertice
    vert_count = 5
    connect_step = 2
    vert_angle_deg = 360 / vert_count
    
    # rotate to look like star on military uniform
    # If you don't rotate, start will be upside down. :)
    rotation = 180

    verts = []

    # Have to find coordinates for 5 points of start to connect them later
    # [1..5]
    for i in range(1, vert_count + 1):
        angle_deg = i * vert_angle_deg * connect_step - rotation

        # center_x to transpose vertice; center_x is center of the star
        # sin to get x coordinate of star outer circle
        # radius to move vertice away from center and construct valid star radius
        point_x = center_x + sin(radians(angle_deg)) * radius
        verts.append(point_x)

        point_y = center_y + cos(radians(angle_deg)) * radius
        verts.append(point_y)

    canvas.create_polygon(verts, fill='black', outline='black')    


def main():
    tk = Tk()

    width = 500
    height = 500

    canvas = Canvas(tk, width=width, height=height)
    canvas.pack()

    # for i in range(20):
    #     random_rectangle(canvas, width, height, random_color())
    #     tk.update()
    #     time.sleep(0.05)

    # canvas.delete('all')

    # for i in range(50):
    #     random_circle(canvas, width, height, random_color())
    #     tk.update()
    #     time.sleep(0.05)

    # canvas.delete('all')

    center_x = 200
    center_y = 200
    radius = 50

    star_pentagon(canvas, center_x, center_y, radius)

    tk.mainloop()


main()
