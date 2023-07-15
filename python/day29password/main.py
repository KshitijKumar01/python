from tkinter import *
from random import *
from tkinter import messagebox
import pyperclip
import json

PATH = "C:\\Users\\acer\\Desktop\\CHANDIGARH UNIVERSITY\\AI ML\\python\\day29password\\logo.png"

FILE_PATH = "C:\\Users\\acer\\Desktop\\CHANDIGARH UNIVERSITY\\AI ML\\python\\day29password\\data.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get() 
    new_data = {
        website : {
            "email" : email,
            "password" : password
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Plase make sure you have filled every field.")
    else:
        try:
            with open(FILE_PATH, "r") as data_file:
                data = json.load(data_file)
            
        except FileNotFoundError:
            with open(FILE_PATH, "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open(FILE_PATH, "w") as data_file:
                json.dump(data, data_file, indent = 4)
                
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_pass():
    website = website_entry.get().lower()
    try:
        with open(FILE_PATH) as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
       if website in data.keys():
            messagebox.showinfo(title="Password Found", message=data[website]["password"])
       else:
           messagebox.showinfo(title="Error", message="There are no details for the site you entered")
    
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file=PATH)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2,  columnspan=2)
email_entry.insert(0, "sunny@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password, width=20)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=20, command=find_pass)
search_button.grid(column=2, row=1)

window.mainloop()