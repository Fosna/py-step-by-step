#!/bin/python3

from tkinter import *
import random

def random_rectangle(canvas, width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)


def random_color():
    return '#{:06x}'.format(random.randint(0, 0xFFFFFF))


def main():
    tk = Tk()

    width = 500
    height = 500

    canvas = Canvas(tk, width=width, height=height)
    canvas.pack()

    random_rectangle(canvas, width, height, random_color())

    tk.mainloop()


main()
