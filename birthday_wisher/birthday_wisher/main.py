import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "ankurana.com007@gmail.com"
MYAPPPASSWORD = "***************"


def get_motivational_quotes():
    with open("quotes.txt", encoding="utf8") as data:
        quotes = data.readlines()
    for n in range(len(quotes)):
        quotes[n] = quotes[n].strip()
    return random.choice(quotes)


def get_bday_quote():
    with open("bday_quotes.txt", encoding="utf8") as data:
        bday_quotes = data.readlines()
    for n in range(len(bday_quotes)):
        bday_quotes[n] = bday_quotes[n].strip()
    return random.choice(bday_quotes)


def send_email(email, message):
    # print(message)
    print(email)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MYAPPPASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{message}".encode("utf8"))


def create_message(name, message):
    with open("bday_msg.txt", encoding="utf8") as data:
        bday_message = data.read()
    bday_message = bday_message.replace("[name]", name)
    bday_message = bday_message.replace("[birthday_quote]", message)
    return bday_message


now = dt.datetime.now()
day = now.day
month = now.month

df = pandas.read_csv("bday_contacts.csv")

# bday_dic = {row.user_name: row.email for (index, row) in df.iterrows()}

for index, row in df.iterrows():
    # print(f"name: {row.user_name} month: {row.month} day: {row.day}")
    if row.month == month and row.day == day:
        send_email(row.email, create_message(row.user_name, get_bday_quote()))






