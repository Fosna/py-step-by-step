from tkinter import *
import random
import time

def random_color():
    return '#{:06x}'.format(random.randint(0, 0xFFFFFF))

def main():
    tk = Tk()

    width = 500
    height = 500

    canvas = Canvas(tk, width=500, height=500)
    canvas.pack()

    rect_id = canvas.create_rectangle(10, 10, 50, 50, fill=random_color())

    for x in range(0, 60):
        canvas.move(rect_id, 5, 0)
        tk.update()
        time.sleep(0.05)

    tk.mainloop()

main()