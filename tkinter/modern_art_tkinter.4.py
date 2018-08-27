#!/bin/python3

from tkinter import *
import random
import time

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
def random_star():
    verts = [10,40,40,40,50,10,60,40,90,40,65,60,75,90,50,70,25,90,35,60]
    canvas.create_polygon(verts)


def main():
    tk = Tk()

    width = 500
    height = 500

    canvas = Canvas(tk, width=width, height=height)
    canvas.pack()

    for i in range(20):
        random_rectangle(canvas, width, height, random_color())
        tk.update()
        time.sleep(0.05)

    canvas.delete('all')

    for i in range(50):
        random_circle(canvas, width, height, random_color())
        tk.update()
        time.sleep(0.05)

    canvas.delete('all')

    random_star()

    tk.mainloop()


main()
