from tkinter import *
import random

def draw_rectangle():
    pass

def main():
    tk = Tk()

    draw_rectangle()

    width = 500
    height = 500

    canvas = Canvas(tk, width=width, height=height)
    canvas.pack()

    tk.mainloop()


main()
