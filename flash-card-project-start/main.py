from tkinter import*
import pandas
import csv
import random
import time
from pandas.core.interchange.dataframe_protocol import DataFrame
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
        original_data = pandas.read_csv("data/french_words.csv")
        words= original_data.to_dict(orient= 'records')
else:
    words = data.to_dict(orient="records")
current_card = {}
#
BACKGROUND_COLOR = "#B1DDC6"
#
words_to_learn = []
def pick_french_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    french_word = current_card["French"]
    canvas.itemconfig(canvas_image, image=file)
    canvas.itemconfig(word_text, text="French", fill="black")
    canvas.itemconfig(translation_text, text=french_word, fill="black")
    window.after(3000, func=card_flip)
    flip_timer = window.after(3000, func=card_flip)



def card_flip():
    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(word_text, text="English", fill = "white")
    canvas.itemconfig(translation_text, text=current_card["English"], fill = "white")

def remove_word():
    words.remove(current_card)
    pick_french_word()
    data = pandas.DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index= False)
    pick_french_word()



window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
#
flip_timer = window.after(3000, func=card_flip)
#
#



#
#
#
#
canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
image = "images/card_front.png"
new = "images/card_back.png"
file = PhotoImage(file=image)
new_image= PhotoImage(file=new)
canvas_image = canvas.create_image(400,263, image=file)
word_text =canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
translation_text =canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(column=0, row=0,columnspan=2)




red_button = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=red_button,highlightthickness=0, command=pick_french_word)
unknown_button.grid(column=0, row=1)

green_button = PhotoImage(file="images/right.png")
known_button = Button(image=green_button, highlightthickness=0,command=remove_word)
known_button.grid(column=1, row=1)

#
#
#
pick_french_word()



window.mainloop()