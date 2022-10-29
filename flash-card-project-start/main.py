import os
from tkinter import *
from tkinter import messagebox

import pandas
import random
# from tkinter.ttk import *
BACKGROUND_COLOR = "#B1DDC6"
FONT_ENG = ("Ariel", 40, "italic")
FONT_FRENCH = ("Ariel", 60, "bold")
COUNT = 5
current_card = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")  # file exist than read only from that
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")  #  or read from org file

flash_cards = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(flash_cards)
    canvas.itemconfig(flash_img, image=img_front)
    canvas.itemconfig(lang, text="French", fill="black")
    canvas.itemconfig(lang_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(flash_img, image=img_back)
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(lang_text, text=current_card["English"], fill="white")


def is_know():
    global flash_cards
    if current_card in flash_cards:
        flash_cards.remove(current_card)
    else:
        messagebox.showinfo(title="INF0", message="you have finished all the words")
        os.remove("./data/words_to_learn.csv")
    next_card()


window = Tk()
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

# Canvas widget
canvas = Canvas()
canvas.configure(width=800, height=526, highlightthickness=0,background=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

flip_timer = window.after(3000, func=flip_card)

# Create a PhotoImage Object
img_front = PhotoImage(file="./images/card_front.png")
img_back = PhotoImage(file="./images/card_back.png")

# Create image inside canvas
flash_img = canvas.create_image(400, 263, image=img_front)

# Create Text inside canvas
lang = canvas.create_text(400, 150, text="French", font=FONT_ENG)
lang_text = canvas.create_text(400, 263, text="French", font=FONT_FRENCH, tags="french")

# Button using the image
img_left = PhotoImage(file="./images/wrong.png")
left_button = Button(image=img_left, highlightthickness=0, command=next_card)
left_button.grid(column=0, row=1)

# Button using the image
img_right = PhotoImage(file="./images/right.png")
left_button = Button(image=img_right, highlightthickness=0, command=is_know)
left_button.grid(column=1, row=1)

next_card()
# count_down(5)


window.mainloop()
df = pandas.DataFrame(flash_cards)
df.to_csv("./data/words_to_learn.csv", index=False)

