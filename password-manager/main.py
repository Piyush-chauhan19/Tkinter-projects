import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)] + \
                    [random.choice(symbols) for har in range(nr_symbols)] + \
                    [random.choice(numbers) for ar in range(nr_numbers)]
    random.shuffle(password_list)

    randon_password = ""
    for char in password_list:
        randon_password += char
    password_input.insert(0, randon_password)
    pyperclip.copy(randon_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if website_input.get() == "" or user_id_input.get() == "" or password_input.get() == "":
        messagebox.showerror(message="Please fill all the details", title="Details missing")
        return
    ok = messagebox.askyesno(title=website_input.get(), message=f"User name: {user_id_input.get()} \n"
                                                                f"Password: {password_input.get()} \n"
                                                                f"Would you like to save??")
    if ok:
        password_record = open('data.txt', 'a')
        password_record.write(
            f"Website: {website_input.get()} , User Id: {user_id_input.get()} , Password: {password_input.get()}\n")
        password_record.close()
        website_input.delete(0, -1)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password manager")
window.config(pady=20, padx=20)

canvas = tk.Canvas(height=200, width=200)
logo = tk.PhotoImage(file='logo.png')
canvas.create_image(80, 100, image=logo)
canvas.grid(row=0, column=1)

# labels
website = tk.Label(text="Website:", font=10)
website.grid(row=1, column=0)
user_id = tk.Label(text="Email/username:", font=10)
user_id.grid(row=2, column=0)
password = tk.Label(text="password:", font=10)
password.grid(row=3, column=0)

# entry boxes
website_input = tk.Entry(width=37)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
user_id_input = tk.Entry(width=37)
user_id_input.grid(row=2, column=1, columnspan=2)
password_input = tk.Entry(width=24)
password_input.grid(row=3, column=1)

# buttons
password_generator = tk.Button(text="generate", command=generate_password)
password_generator.grid(row=3, column=2)
add = tk.Button(text="Add", width=37, command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
