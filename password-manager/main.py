from tkinter import *
from datetime import datetime
from tkinter import messagebox
import random
import pyperclip
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

# ---------------------------- SAVE PASSWORD ------------------------------- #


def write_to_secure_file():
    # global password_mng_data
    # temp_dic = {}
    website_value = web_entry.get()  # get the required data from the entry field
    username_value = user_entry.get()
    password_value = pass_entry.get()
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    msg = ""
    is_ok = False
    # temp_dic["username"] = username_value
    # temp_dic["password"] = password_value
    # password_mng_data[website_value] = temp_dic
    if website_value == "":
        msg += "Your website field is empty!\n"
    if username_value == "":
        msg += "Your username field is empty!\n"
    if password_value == "":
        msg += "Your password field is empty\n"

    if website_value == "" or username_value == "" or password_value == "":
        messagebox.showinfo(title="OOPS!", message=f"{msg}")
    else:
        is_ok = messagebox.askokcancel(title="Save Info", message=f"website: {website_value}\n"
                                       f"username: {username_value}\npassword: {password_value}\n")  # This return T/F

    if is_ok:
        with open("../../../Users/Amit Rana/OneDrive/Documents/AmitRana/SecureCodes/secure_file_codes.txt", mode="a")\
                    as data:
            data.write(f"[INFO]:{date_time} --> website: {website_value} | username: {username_value} "
                       f"| password: {password_value}\n")
            pass_entry.delete(0, END)  # Deletes data from entry start 0 and till end
            web_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website Label
web_label = Label(text="Website:")
web_label.grid(column=0, row=1, sticky="w")

# Username Label
user_label = Label(text="Email/User Name:")
user_label.grid(column=0, row=2, sticky="w")

# Password Label
pass_label = Label(text="Password:", anchor="w")  # can use anchor to move the text to left corner here just for show
pass_label.grid(column=0, row=3, sticky="w")  # sticky attribute sets the alignment to west in a grid

# website text input field
web_entry = Entry(width=55)
web_entry.grid(column=1, row=1, columnspan=2, sticky="w")  # column span club columns together
web_entry.focus()

# username text input field
user_entry = Entry(width=55)
user_entry.grid(column=1, row=2, columnspan=2, sticky="w")
user_entry.insert(0, "amitrana.com007@yahoo.com")  # insert data into entry at 0

# password text input field
pass_entry = Entry(width=35)
pass_entry.grid(column=1, row=3, sticky="w")


# Generate button
gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(column=2, row=3, sticky="ew")

# Add button
add_button = Button(text="Add", width=36, command=write_to_secure_file)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")


window.mainloop()
