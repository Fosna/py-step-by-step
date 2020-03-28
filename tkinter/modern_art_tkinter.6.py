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
def random_star(canvas):
    center_x = 200
    center_y = 200
    radius = 50

    vert_count = 5

    horizontal_to_vertex_angle_deg = 360 / vert_count
    # rotate to look like star on military uniform
    rotation = 180

    verts = []

    for i in range(1, vert_count + 1):
        angle_deg = i * horizontal_to_vertex_angle_deg * 2 - rotation
        
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

    random_star(canvas)

    tk.mainloop()


main()
