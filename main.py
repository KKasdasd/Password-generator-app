from tkinter import Tk, Label, Button, PhotoImage, Canvas, Entry


ENTRY_WIDTH = 35

def find_password():
    pass

def generate_password():
    pass

def add():
    pass

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