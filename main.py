import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

#this function generates a random password for the website entered.
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    pw_entry.insert(0, password)
    pyperclip.copy(password)



#this function saves the website information to a json file.
def save():
    website = website_entry.get()
    username = uname_entry.get()
    password = pw_entry.get()

    user_data = {website: {"email": username, "password": password}}

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty")
        return
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
                data.update(user_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(user_data, file, indent=4)
        else:
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, 'end')
            pw_entry.delete(0, 'end')
            website_entry.focus()


def find_password():
    website = website_entry.get()

    try:
        with open("data.json", mode="r") as file:
            data_dict = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found!")
        return

    try:
        email = data_dict[website]["email"]
    except KeyError:
        messagebox.showinfo(title="Error", message="No data available for this website")
    else:
        pw = data_dict[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {pw}")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


#creating labels
website_label = Label(text="Website")
website_label.grid(column=0, row=1)

uname_label = Label(text="Email/Username")
uname_label.grid(column=0, row=2)

pw_label = Label(text="Password")
pw_label.grid(column=0, row=3)


#creating entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

uname_entry = Entry(width=39)
uname_entry.grid(column=1, row=2, columnspan=2, sticky="w")
uname_entry.insert(0, "aaryan@gmail.com")

pw_entry = Entry(width=21)
pw_entry.grid(column=1, row=3, sticky="w")


#creating buttons
gen_pw_button = Button(text="Generate Password", command=generate_password)
gen_pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
