import tkinter as tk
from random import randint


def create_dice():
    """
    Creates the dice with all the sides drawn in a list.
    The sides are drawn by the draw_dice function.

    :return: dice list
    """
    dice = list()
    dice.append(draw_dice('dot0'))  # empty
    dice.append(draw_dice('dot4'))  # center dot --> 1
    dice.append(draw_dice('dot3', 'dot5'))  # dice head 2
    dice.append(draw_dice('dot2', 'dot4', 'dot6'))  # dice head 3
    dice.append(draw_dice('dot1', 'dot2', 'dot6', 'dot9'))  # dice head 4
    dice.append(draw_dice('dot1', 'dot2', 'dot4', 'dot6', 'dot9'))  # dice head 5
    dice.append(draw_dice('dot1', 'dot2', 'dot3', 'dot5', 'dot6', 'dot9'))  # dice head 6
    return dice


def draw_dice(*args):
    """
    Creates the individual heads passed in through the 
    create_dice function.

    :param args: string(s) for certain dots for certain heads
    :return: c canvas
    """
    w, h = 100, 100 # sets width and height
    x, y, r =27,27, 20 # sets x, y, and radius
    c = tk.Canvas(root, width=w, height=h, bg='black') # creates canvas c
    #c.grid(row = 2,column = 3)
    #Dictionary containing lambda functions to draw dots on canvas c
    dots = {
        'dot0': lambda x, y, r: c,
        'dot1': lambda x, y, r: c.create_oval(x, y, x + r, y + r, fill='red'),
        'dot2': lambda x, y, r: c.create_oval(x +35, y, (x +35) + r, y + r, fill='red'),
        'dot3': lambda x, y, r: c.create_oval(x, y + 16, x + r, (y + 16) + r, fill='red'),
        'dot4': lambda x, y, r: c.create_oval(x + 16, (y + 16), (x + 16) + r, (y + 16) + r, fill='red'),
        'dot5': lambda x, y, r: c.create_oval(x +35, (y + 16), (x +35) + r, (y + 16) + r, fill='red'),
        'dot6': lambda x, y, r: c.create_oval(x, y +39, x + r, (y +39) + r, fill='red'),
        'dot9': lambda x, y, r: c.create_oval(x +35, y+39, (x +35) + r, (y +39) + r, fill='red')
    }

    for arg in args:
        dots.get(arg)(x, y, r) # Gets the dictionary keys while passing in x, y, and r values

    return c


def click():
    """
    Performs the operation of clicking the button. This will roll through
    the different dice heads

    :return: None
    """
    t = 100 # start with a time delay of 100 ms and increase it as the dice rolls
    stop = randint(13, 18) # chooses random number between 13 - 17
    for x in range(stop):
        dice_index = x % 6 + 1 # gets the randomly selected dice head by modulo
        dice_list[dice_index].grid(row=1, column=0, columnspan=3)
        root.update()
        if x == stop - 1:
            # set text to the selected result
            text.set(str(x % 6 + 1))
            break
        root.after(t, dice_list[dice_index].grid_forget()) # forgets the grid and restarts
        t += 25


# create the window form
root = tk.Tk()
root.title("Dice Roll")
root.geometry('500x400')
# StringVar() updates result label automatically
text = tk.StringVar()

# set initial value of text
text.set("")

# create the result label
result = tk.Label(root, textvariable=text, fg='black')
result.grid(row=3, column=0, columnspan=3)
dice_list = create_dice()

# start with an empty canvas
dice_list[0].grid(row=1, column=0, columnspan=3)

button1 = tk.Button(root, text="Roll", command=click)
button1.grid(row=5, column=5, padx=3, pady=3)
button2 = tk.Button(root, text="Quit", command=root.destroy)
button2.grid(row=5, column=7, pady=3)

# start of program event loop
root.mainloop()
