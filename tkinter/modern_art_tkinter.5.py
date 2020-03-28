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
    verts = []
    center_x = 200
    center_y = 200
    radius = 50

    min_x = center_x - radius
    max_x = center_x + radius

    point_count = 5
    step = int(360 / point_count)


    verts_x = []
    verts_y = []
    for angle_deg in range(0, 360, step):
        point_x = center_x + sin(radians(angle_deg)) * radius
        verts.append(point_x)
        verts_x.append(point_x)

        point_y = center_y + cos(radians(angle_deg)) * radius
        verts.append(point_y)
        verts_y.append(point_y)

    # canvas.create_polygon(verts, fill='', outline='black')

    start_angle_deg = 36
    
    verts2 = []
    verts2_x = []
    verts2_y = []
    pointy_radius = radius * 2

    for angle_deg in range(start_angle_deg, 360 + start_angle_deg, step):
        point_x = center_x + sin(radians(angle_deg)) * pointy_radius
        verts2.append(point_x)
        verts2_x.append(point_x)

        point_y = center_y + cos(radians(angle_deg)) * pointy_radius
        verts2.append(point_y)
        verts2_y.append(point_y)

    # canvas.create_polygon(verts2, fill='', outline='black')

    # verts_star = []
    # for i in range(len(verts2),2):
    #     for j in range(i,len(verts2),2):
    #         canvas.create_line(verts2[i],verts2[i+1],verts2[j],verts2[j+1])

    star_verts = []
    for i in range(len(verts_x)):
        star_verts.append(verts_x[i])
        star_verts.append(verts_y[i])
        star_verts.append(verts2_x[i])
        star_verts.append(verts2_y[i])

    canvas.create_polygon(star_verts, fill='', outline='black')

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
