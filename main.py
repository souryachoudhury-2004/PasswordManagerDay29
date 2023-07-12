from tkinter import *
from tkinter import messagebox  # Messagebox must be imported separately
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "~`! @#$%^&*()_-+={[}]|:;'<,>.?/"
pass_combo = letters+digits+symbols


# Function to generate password
def generate_password():
    # Creates password
    generated_code = ""
    for iteration in range(0, random.randint(5, 20)):
        generated_code += random.choice(pass_combo)

    # Clears password entry and displays generated password in it's place
    password_input.delete(0, END)
    password_input.insert(0, generated_code)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    with open("password_data.txt") as data:
        pass_codes = data.readlines()

    Email = email_input.get()
    Website = website_name_input.get()
    Password = password_input.get()

    # Checking whether all entries have been filled
    go_ahead = False
    if 0 in [len(Website), len(Email), len(Password)]:
        messagebox.showwarning(title="Warning!", message="Please don't leave any field empty!")
    else:

        pass_codes.append(Website + " | " + Email + " | " + Password + "\n")

        go_ahead = messagebox.askokcancel(title="Confirmation",
                                          message=f"The following details shall be saved: \n Website: {Website}\n Email/Username: {Email}\n Password: {Password}\n Is it okay to save?")

    if go_ahead:

        with open("password_data.txt", "w") as data:
            for item in pass_codes:
                data.write(item)

        # Confirming that it has been saved
        messagebox.showinfo(title="Success", message="Details saved!")

        # Clearing entries
        website_name_input.delete(0, END)
        password_input.delete(0, END)

    # Focusing cursor back on website entry
    website_name_input.focus()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=100, pady=100)
window.title("MyPass Password Manager")

# Canvas for logo
canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Website label and input
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, pady=10)

website_name_input = Entry(width=50)
website_name_input.grid(row=1, column=1, columnspan=2, pady=10)

# Focuses cursor on website name entry
website_name_input.focus()

# Email name and input
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, pady=10)

email_input = Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2)
# Inserts common value into email entry
email_input.insert(0, "sourya@gmail.com")

# Password name and input
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, pady=10)

password_input = Entry(width=32)
password_input.grid(row=3, column=1)

# Generate and add buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, pady=10)

add_button = Button(text="Add", width=50, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
