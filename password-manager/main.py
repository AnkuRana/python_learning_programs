from tkinter import *
from tkinter.ttk import *   # this class gives style to buttons
from datetime import datetime
from tkinter import messagebox
import random
import pyperclip
import json
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)  # This module let us copy whatever is there in clipboard
# ---------------------------- SEARCH PASSWORD ------------------------------- #


def option_changed(*args):
    return menu.get()


def get_list_websites():
    websites = []
    try:
        with open("../../../Users/Amit Rana/OneDrive/Documents/AmitRana/SecureCodes/secure_file_codes.json") \
                as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="INFO", message="Database is empty or not created!")
    else:
        websites = [website for website in data]
    return websites


def search_password():
    website_value = option_changed()
    # website_value = list_box.get(list_box.curselection())
    # website_value = web_entry.get().lower()  # get the required data from the entry field
    if website_value == "" or website_value == "select website":
        messagebox.showinfo(title="INFO", message="Please select the website name to search database!")
    else:
        try:
            with open("../../../Users/Amit Rana/OneDrive/Documents/AmitRana/SecureCodes/secure_file_codes.json",
                      mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="INFO", message="Database is empty or not created!")
        else:
            # Check if any key is missing and throw warning or message
            if website_value in data:
                user_name = data[website_value]['username']
                password = data[website_value]['password']
                date_time = data[website_value]['datetime']
                messagebox.showinfo(title=f"Website: {website_value}", message=f"Website: {website_value}\n"
                                                                               f"UserName: {user_name}\n"
                                                                               f"Password: {password}\n"
                                                                               f"Saved Date: {date_time}\n\n"
                                                                               f"Click ok to copy Password!")
                pyperclip.copy(password)
            else:
                messagebox.showinfo(title="Website data not saved", message=f"Data for {website_value} not found!")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def write_to_secure_file():
    # global password_mng_data
    # temp_dic = {}
    website_value = web_entry.get().lower()  # get the required data from the entry field
    username_value = user_entry.get()
    password_value = pass_entry.get()
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    msg = ""
    is_ok = False
    # temp_dic["username"] = username_value
    # temp_dic["password"] = password_value
    # password_mng_data[website_value] = temp_dic
    new_data = {
        website_value: {
            "username": username_value,
            "password": password_value,
            "datetime": date_time,
        }
    }
    if website_value == "":
        msg += "Your website field is empty!\n"
    if username_value == "":
        msg += "Your username field is empty!\n"
    if password_value == "":
        msg += "Your password field is empty\n"

    # if  there are empty values for the field that show warning
    if website_value == "" or username_value == "" or password_value == "":
        messagebox.showinfo(title="OOPS!", message=f"{msg}")
    else:
        is_ok = messagebox.askokcancel(title="Save Info", message=f"website: {website_value}\n"
                                       f"username: {username_value}\npassword: {password_value}\n")  # This return T/F
    #  if the data entered is not empty and user wanted to save the data
    if is_ok:
        try:
            with open("../../../Users/Amit Rana/OneDrive/Documents/AmitRana/SecureCodes/secure_file_codes.json",
                      mode="r") as data_file:
                current_data = json.load(data_file)  # loading the json file to current data
                current_data.update(new_data)   # updating the current data with the new data
        except FileNotFoundError:
            with open("../../../Users/Amit Rana/OneDrive/Documents/AmitRana/SecureCodes/secure_file_codes.json",
                      mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("../../../Users/Amit Rana/OneDrive/Documents/AmitRana/SecureCodes/secure_file_codes.json",
                      mode="w") as data_file:
                json.dump(current_data, data_file, indent=4)  # writing the updated current data to json
        finally:
            pass_entry.delete(0, END)  # Deletes data from entry start 0 and till end
            web_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

# Canvas Widget
canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website Label
web_label = Label(text="Website:", background=YELLOW, font=(FONT_NAME, 10, "bold"))
web_label.grid(column=0, row=2, sticky="w")

# listbox Label
listbox_label = Label(text="Database:", background=YELLOW, font=(FONT_NAME, 10, "bold"))
listbox_label.grid(column=0, row=1, sticky="w")

# Username Label
user_label = Label(text="Email/User Name:", background=YELLOW, font=(FONT_NAME, 10, "bold"))
user_label.grid(column=0, row=3, sticky="w")

# Password Label # can use anchor to move the text to left corner here just for show
pass_label = Label(text="Password:", background=YELLOW, anchor="w", font=(FONT_NAME, 10, "bold"))
pass_label.grid(column=0, row=4, sticky="w")  # sticky attribute sets the alignment to west in a grid

# website text input field
web_entry = Entry(width=33)
web_entry.grid(column=1, row=2, columnspan=2, sticky="ew")  # column span club columns together
web_entry.focus()

# get stored website
list_stored_websites = get_list_websites()

# Menu
menu = StringVar()
dropdown = OptionMenu(window, menu, "select website", *list_stored_websites)
dropdown.config(width=29)
dropdown.grid(column=1, row=1, columnspan=2, sticky="w")

# username text input field
user_entry = Entry(width=35)
user_entry.grid(column=1, row=3, columnspan=2, sticky="ew")
user_entry.insert(0, "amitrana.com007@yahoo.com")  # insert data into entry at 0

# password text input field
pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=4, sticky="w")

# Generate button
gen_button = Button(text="Generate Password", width=20, command=generate_password)
gen_button.grid(column=2, row=4, sticky="w")

# Add but
add_button = Button(text="Add", width=36, command=write_to_secure_file)
add_button.grid(column=1, row=5, columnspan=2, sticky="ew")

# Search button
search_button = Button(text="Search", width=20, command=search_password)
search_button.grid(column=2, row=1, sticky="w")


window.mainloop()
