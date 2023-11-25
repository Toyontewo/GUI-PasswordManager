from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_letters = [choice(letters) for _ in range(randint(3, 5))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_num = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_num
    shuffle(password_list)
    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_command():
    website = url_input.get()
    username = user_name_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Field can't be empty")
    else:
        try:
            with open("data_file.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data_file.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data_file.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            url_input.delete(0, END)
            password_entry.delete(0, END)
            url_input.focus()
# ---------------------------- SEARCH ACCOUNT/PASSWORD ------------------------------- #
def find_password():
    website = url_input.get()
    try:
        with open("data_file.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="No Datafile found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(message=f"No Details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("Arial", 14))
website_label.grid(row=1, column=0)

url_input = Entry(width=20)
url_input.focus()
url_input.grid(row=1, column=1)

search_btn = Button(text="Search", width=11, command=find_password)
search_btn.grid(row=1, column=2)

user_name = Label(text="Email/Username:", font=("Arial", 14))
user_name.grid(row=2, column=0)

user_name_entry = Entry(width=35)
user_name_entry.grid(row=2, column=1, columnspan=2)
user_name_entry.insert(0, "toyob4lyf@gmail.com")

password_label = Label(text="Password:", font=("Arial", 13))
password_label.grid(row=3, column=0)

password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

generate_btn = Button(text="Generate Password", width=11, command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=33, command=add_command)
add_btn.grid(row=4, column=1, columnspan=2)




window.mainloop()