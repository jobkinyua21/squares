####REQUIREMENTS#####
# use pip install pynput
# pip install tkinter
# pip install random


##IMPORTS###
from pynput.mouse import Listener
from pynput import mouse, keyboard
import logging
from tkinter import *
import random
import sys

#### VARIABLES DECLARATION  ########
color_square = ['red', 'blue', 'green', 'purple', 'grey']
start_x = None
start_y = None
i = 0
width = 50
height = 50
fill_color = str
center_point = [0, 0]
label = str

#### build tkinter GUI#####
root = Tk()
root.geometry('500x500')

c = Canvas(root, height=500, width=500)
c.pack()


#####creating a event######

def on_click(event, pressed):
    if pressed:
        x, y = event.x, event.y


def motion(event):
    global i
    # while the value of i is less than 6 this loop will keep runnning
    while (i < 6):
        # value of i icreased by 1
        i += 1
        # getting random color from the color array
        fill_color = random.choice(color_square)
        x, y = event.x, event.y

        # finding the coordinate of the upper left side of the rectangle
        start_x = x - 25
        start_y = y - 25
        # create a rectangle where start_x and start_y are the top left coordinate
        # start_x +height and start_y + width give us the bottom right coordinates
        shape = c.create_rectangle(
            start_x, start_y, start_x + height, start_y + width, fill=fill_color)
        text = c.create_text(x, y, text=i, fill="white")

        if (i < 6):

            label = Label(
                c, text=f"Click to draw a square: {6 - i} left").place(x=0, y=5, width=500)
        else:
            label = Label(c, text=f"Click to quit").place(x=0, y=5, width=500)
        return i
    else:
        sys.exit()


# this function initialize the mouse listener for a click event
def create_square(center_point, width, height, fill_color, label):
    with mouse.Listener(on_click=on_click) as listener:
        c.bind('<Button>', motion)


initial_label = Label(c, text=f"Click to draw a square:").place(x=0, y=5, width=500)

create_square(center_point, width, height, fill_color, label)
root.mainloop()
