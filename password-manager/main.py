from string import whitespace
from tkinter import *
from tkinter import messagebox
import random
from six import text_type
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for x in range(nr_letters)]

    number_list = [random.choice(numbers) for k in range(nr_numbers)]
    symbol_list = [random.choice(symbols) for y in range(nr_symbols)]

    password_list = letter_list + number_list + symbol_list

    random.shuffle(password_list)

    password = ''.join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password, }}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Read data
                data = json.load(data_file)
                # update data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            # save data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                # print(data)
        finally:
            clear_screen()


def clear_screen():
    web_entry.delete(0, "end")
    email_entry.delete(0, "end")
    password_entry.delete(0, "end")


def find_password():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            data= json.load(data_file)


    else:
        if website in data:
            password = data[website]["password"]
            email = data[website]["email"]
            messagebox.showinfo(title=f"{website}", message=f"website:{website}\n password = {password}")
        elif website not in data:
            messagebox.showinfo(title="Oops", message=f"No details for the {website} exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
file = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=file)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_label.focus()

email_label = Label(text="Email/Username:", width=20)
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

generate_button = Button(text="Generate Password", command=generate_password, width=11)
generate_button.grid(column=2, row=3)

search_button = Button(text="Search", width=11, command=find_password)
search_button.grid(column=2, row=1)

web_entry = Entry(width=25)
web_entry.grid(column=1, row=1, )

email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "johndoe@live.com")

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

window.mainloop()