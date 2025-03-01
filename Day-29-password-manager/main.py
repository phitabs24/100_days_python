from tkinter import *
import pyperclip
import messagebox
from random import randint, choice, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_str = password_entry.get()

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for symbol in range(randint(2, 4))]
    password_list += [choice(numbers) for number in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    if len(password_str) != 0:
        password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Opps", message="No empty field")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            delete()


def delete():
    web_entry.delete(0, END)
    password_entry.delete(0, END)


def find_password():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            email = data[website]["email"]
            password = data[website]["password"]
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File found")
    except KeyError:
        messagebox.showinfo("Error", "No details for the website exists")

    else:
        pyperclip.copy(password)
        messagebox.showinfo(website, f"Email: {email}\nPassword: {password}\n\nPassword copied to clipboard")
        delete()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text="Website:", padx=20)
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", padx=20)
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", padx=-10)
password_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=33)
web_entry.grid(row=1, column=1)
web_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "phitabs24@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", cursor="hand2", command=find_password, width=14)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Password", cursor="hand2", command=generate_password)
generate_button.grid(row=3, column=2)

save_button = Button(text="Add", cursor="hand2", width=44, command=save_password)
save_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
