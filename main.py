from tkinter import Tk, Label, Button, PhotoImage, Canvas, Entry, messagebox, END
import json
from random import choice, randint, shuffle
import pyperclip
ENTRY_WIDTH = 35



# -------------------- SEARCH PASSWORD -------------------- #

def find_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title=website, message="Website field is empty")
        return
    try:
        with open("./Passwords_data.json", "r") as password_file:
            data = json.load(password_file)

    except FileNotFoundError:
        messagebox.showerror(
            title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword:{password}")
        else:
            messagebox.showerror(title="Error",
                                 message="Website Not Found")

def generate_password():
    password_entry.delete(0, END)
    lower_letters = [chr(x) for x in range(97, 123)]
    numbers = [chr(x) for x in range(48, 58)]
    symbols = [chr(x) for x in range(33, 44) if not (x == 44 or x == 39)]

    password_letters = [choice(lower_letters) for _ in range(randint(8, 10))]
    password_letters.append(choice(lower_letters).upper())
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# -------------------- SAVE PASSWORD -------------------- #
def add():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Fields cannot be empty")
        return
    is_ok = messagebox.askokcancel(
    message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?")

    if is_ok:
        try:
            with open("./data/Passwords_data.json", "r") as password_file:
                data = json.load(password_file)
        except FileNotFoundError:
            with open("./data//Passwords_data.json", "w") as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            data.update(new_data)
            with open("./data/Passwords_data.json", "w") as password_file:
                json.dump(data, password_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# -------------------- UI SETUP -------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.columnconfigure(1, pad=50)


canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="./images/logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# entry's
website_entry = Entry(width=ENTRY_WIDTH)
website_entry.grid(row=1, column=1, sticky="w")
website_entry.focus()

email_entry = Entry(width=ENTRY_WIDTH)
email_entry.grid(row=2, column=1, sticky="w")
email_entry.insert(0, "example@gmial.com")

password_entry = Entry(width=ENTRY_WIDTH)
password_entry.grid(row=3, column=1, sticky="w")

# Buttons
search_button = Button(text="Search", command=find_password, width=15)
search_button.grid(row=1, column=2, pady=5)
generate_password_button = Button(
    text="Generate Password", command=generate_password, width=15)
generate_password_button.grid(row=2, column=2, sticky="w", pady=5)

add_button = Button(text="Add", width=15, command=add)
add_button.grid(row=3, column=2, sticky="w", pady=5)

window.mainloop()