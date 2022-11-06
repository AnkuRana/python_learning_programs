import requests
from datetime import datetime
import smtplib
import time
import os

MY_LAT = 30.786335
MY_LONG = 76.798265
USERNAME = "ankurana.com007@gmail.com"
APP_PASSWORD = os.environ.get("EMAIL_PASS")

MESSAGE = "Hey ISS is above you!,\n It's dark and perfect time to catch a glimpse of space station in the sky!" \
          " \n from Amit Rana\n"\
          "Tracking the International Space Station"
CONTACTS = ["amitrana.com0007@gmail.com", "ayushkumar9533@gmail.com", "nitinrananr34@gmail.com",
            "mayankocts92@gmail.com"]


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}


def send_email(email, message):
    # print(message)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=APP_PASSWORD)
        connection.sendmail(from_addr=USERNAME,
                            to_addrs=email,
                            msg=f"Subject:International Space Station is nearby at (latitude:{MY_LAT} ,"
                                f" longitude:{MY_LONG})!\n\n{message}".encode("utf8"))


def get_iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    return latitude, longitude


def get_sun_rise_set():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return sunrise, sunset


def current_time():
    return datetime.utcnow()


def is_currently_dark():
    sun_time = get_sun_rise_set()
    # print(sun_time)
    now = current_time()
    # print(now.hour)
    if sun_time[1] <= now.hour or now.hour <= sun_time[0]:
        return True
    else:
        return False


def is_iss_within_range():
    location = get_iss_location()
    if MY_LAT - 10 <= location[0] <= MY_LAT + 10 and MY_LONG - 10 <= location[1] <= MY_LONG + 10:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_iss_within_range():
        for contact in CONTACTS:
            send_email(contact, MESSAGE)



