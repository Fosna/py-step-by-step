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

    canvas = Canvas(tk, width=500, height=500)
    canvas.pack()

    canvas.create_line(0, 0, 500, 500)
    canvas.create_rectangle(10, 10, 50, 50)

    for i in range(5):
        random_rectangle(canvas, width, height, random_color())

    canvas.create_text(100, 100, text='Hello World', fill=random_color(), font=('Arial', 30), anchor=NW)

    grumpy_cat_img = PhotoImage(file='./cat_grumpy.gif')
    canvas.create_image(100, 200, anchor=NW, image=grumpy_cat_img)

    canvas.create_arc(10, 10, 110, 110, extent=359, style=ARC)


    tk.mainloop()

main()