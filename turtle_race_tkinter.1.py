#!/bin/python3

from tkinter import *
import random
import time

def random_color():
    return '#{:06x}'.format(random.randint(0, 0xFFFFFF))


def create_triangle(canvas, x, y, width, height, fill_color):
    x2 = x + width
    y2 = y + height / 2
    x3 = x
    y3 = y + height

    canvas.create_polygon(x, y, x2, y2, x3, y3, fill=random_color())


def main():
    tk = Tk()

    width = 500
    height = 500

    canvas = Canvas(tk, width=width, height=height)
    canvas.pack()

    x = 10
    y = 40
    triangle_width = 20
    triangle_height = 20

    canvas.create_polygon(10, 10, 15, 15, 10, 20, fill=random_color())

    create_triangle(canvas, x, y, triangle_width, triangle_height, random_color())

    tk.mainloop()


main()
