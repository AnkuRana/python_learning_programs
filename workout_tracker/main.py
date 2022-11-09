import requests
import os
from datetime import datetime
app = os.environ[""]
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

NUTRI_API = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL = os.environ.get("SHEETY_URL")

# parameters = {
#     "query": input("What kind of workout did you do!: ").lower(),
#     "gender": input("Gender: ").lower(),
#     "weight_kg": float(input("Weight in kgs: ")),
#     "height_cm": float(input("Height in cms: ")),
#     "age": int(input("Age: "))
# }
parameters_nut = {
    "query": input("What kind of workout did you do!: ").lower(),
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 178,
    "age": 28
}

headers_nut = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
headers_sheety = {
    "Content-Type": "application/json",
    "Authorization": SHEETY_TOKEN
}
activities_data = {}
response_nut = requests.post(url=NUTRI_API, json=parameters_nut, headers=headers_nut)
response_nut.raise_for_status()
print(response_nut.json()["exercises"])
today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

exercises_data = response_nut.json()["exercises"]

for exercise in exercises_data:
    body = {
        "workout": {
            "date": today,
            "time": time,
            "duration": exercise["duration_min"],
            "exercise": exercise["name"].title(),
            "calories": exercise["nf_calories"]

        }
    }
    response_sheety = requests.post(url=SHEETY_URL, json=body, headers=headers_sheety)
    response_sheety.raise_for_status()
    print(response_sheety.json())
