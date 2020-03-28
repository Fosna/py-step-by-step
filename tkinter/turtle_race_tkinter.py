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

    return canvas.create_polygon(x, y, x2, y2, x3, y3, fill=random_color())


def main():
    tk = Tk()

    width = 500
    height = 500

    canvas = Canvas(tk, width=width, height=height)
    canvas.pack()

    turtle_count = 3
    turtle_start_x = 30
    turtle_x = turtle_start_x
    turtle_y = 130
    turtle_width = 20
    turtle_height = 20
    turtle_vertical_margin = turtle_height + 10

    line_horizontal_margin = 20
    line_x = turtle_x + line_horizontal_margin + 10
    line_y = turtle_y - 10
    line_text_y = line_y - 10
    line_length = turtle_vertical_margin * turtle_count + 10

    # race track
    for i in range(0, 14):
        canvas.create_text(line_x, line_text_y, text=str(i))
        canvas.create_line(line_x, line_y, line_x, line_y + line_length)
        
        line_x += line_horizontal_margin

        tk.update()
        time.sleep(0.05)

    # turtles
    turtles = []
    for i in range(turtle_count):
        turtle_color = random_color()
        # turtle_color = '#00FF00'
        turtle_id = create_triangle(canvas, turtle_x, turtle_y, turtle_width, turtle_height, turtle_color)
        turtles.append({
            'id': turtle_id,
            'x': turtle_x,
            'y': turtle_y,
            'color': turtle_color
        })
        
        turtle_y += turtle_vertical_margin

        tk.update()
        time.sleep(0.05)

    # race
    for turn in range(100):
        for turtle in turtles:
            turtle_move_x = random.randint(1, 5)
            turtle['x'] += turtle_move_x

            line_y = turtle['y'] + turtle_height / 2 
            canvas.create_line(turtle_start_x, line_y, turtle['x'], line_y, fill=turtle['color'])

            # print(turtle['id'], turtle['color'])

            canvas.move(turtle['id'], turtle_move_x, 0)

        tk.update()
        time.sleep(0.05)

    tk.mainloop()


main()
