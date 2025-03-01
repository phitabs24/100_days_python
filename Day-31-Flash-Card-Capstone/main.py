from tkinter import *
# from tkinter import messagebox
import pandas
from random import choice, shuffle, randint

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



# Image Asset
RIGHT_IMAGE = PhotoImage(file="images/right.png")
WRONG_IMAGE = PhotoImage(file="images/wrong.png")
FRONT_IMAGE = PhotoImage(file="images/card_front.png")
BACK_IMAGE = PhotoImage(file="images/card_back.png")
current_card = None
FONT_NAME = "Arial"
LANGUAGES = ["French", "English"]

try:
    word_list = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_list = pandas.read_csv("data/french_words.csv")
finally:
    to_learn = word_list.to_dict(orient="records")

# Flash card canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=FRONT_IMAGE)

# Text
card_title = canvas.create_text(400, 150, text=f"{choice(LANGUAGES)}", font=(FONT_NAME, 40, "italic"))
card_text = canvas.create_text(400, 263, text=f"{choice(to_learn)["French"]}", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

def new_card():
    global current_card, flip_timer
    flip_timer = window.after_cancel(flip_timer)

    current_card = choice(to_learn)
    french_word = current_card["French"]

    canvas.itemconfig(canvas_image, image=FRONT_IMAGE)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=french_word, fill="black")

    flip_timer = window.after(3000, flip_card)

    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv",index=False)


def flip_card():
    english_word = current_card["English"]
    canvas.itemconfig(canvas_image, image=BACK_IMAGE)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=english_word, fill="white")

def skip():
    global current_card
    print(len(to_learn))
    new_card()

def is_known():
    global current_card, to_learn
    to_learn.remove(current_card)
    print(len(to_learn))
    new_card()

# Buttons
right_button = Button(image=RIGHT_IMAGE, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_button = Button(image=WRONG_IMAGE, highlightthickness=0, command=skip)
wrong_button.grid(row=1, column=0)

flip_timer = window.after(3000, flip_card)
new_card()

window.mainloop()
