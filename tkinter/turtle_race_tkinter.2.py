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

    turtle_count = 6
    turtle_x = 30
    turtle_y = 130
    triangle_width = 20
    triangle_height = 20
    turtle_vertical_margin = triangle_height + 10
    

    line_horizontal_margin = 20
    line_x = turtle_x + line_horizontal_margin + 10
    line_y = turtle_y - 10
    line_text_y = line_y - 10
    line_length = turtle_vertical_margin * turtle_count + 10

    for i in range(turtle_count):
        create_triangle(canvas, turtle_x, turtle_y, triangle_width, triangle_height, random_color())
        turtle_y += turtle_vertical_margin
        tk.update()
        time.sleep(0.05)

    for i in range(1, 15):
        canvas.create_text(line_x, line_text_y, text=str(i))
        canvas.create_line(line_x, line_y, line_x, line_y + line_length)
        
        line_x += line_horizontal_margin

        tk.update()
        time.sleep(0.05)

    tk.mainloop()


main()
