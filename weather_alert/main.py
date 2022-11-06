import requests
from twilio.rest import Client
import os

ACCOUNT_SID = "ACdb021b083648d0d9d2efe44b28c47847"
AUTH_TOKEN = os.environ.get("TWIL_AUTH")
TWILIO_PHONE = "+16295002463"
global description

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# OPEN_WEATHER_API = "https://pro.openweathermap.org/data/2.5/forecast/climate"
OPEN_WEATHER_API = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/hourly"
APP_ID = os.environ.get("RAPID_AUTH_KEY")

parameters = {
    "lat": 30.785633,
    "lon": 76.794442,
    "hours": 16
    # "cnt": 7
}

headers = {
    "X-RapidAPI-Key": APP_ID,
    "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
  }

response = requests.get(OPEN_WEATHER_API, params=parameters, headers=headers)
response.raise_for_status()
weather_data_hourly = response.json()["data"]
is_rain = False
for hour in weather_data_hourly:
    # print(type(hour['weather']['code']))
    if hour['weather']['code'] < 700:
        is_rain = True

contacts = ["+DUMMY_1", "+DUMMY_2"]

for contact in contacts:
    if is_rain:
        message = client.messages.create(
            messaging_service_sid='MG061bacffe4c02103de2b2ac4293c49d4',
            body='Its probably going to rain today bring an umbrella',
            to=contact
        )
    print(message.status)
