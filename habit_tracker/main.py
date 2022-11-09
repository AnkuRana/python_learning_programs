import requests
from datetime import datetime
import os

PIXELA_USER_ENDPT = "https://pixe.la/v1/users"
USERNAME = "ankurana"
TOKEN = os.environ.get("PIX_TOKEN")
GRAPH_ID = "day-py-streak"
GRAPH_ENDPT = f"{PIXELA_USER_ENDPT}/{USERNAME}/graphs"
PIXEL_POST_ENDPT = f"{PIXELA_USER_ENDPT}/{USERNAME}/graphs/{GRAPH_ID}"

parameters = {
    "token": TOKEN,
    "username": "ankurana",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": "day-py-streak",
    "name": "Daily Tracker",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
    "timezone": "Asia/Calcutta"
}
user_header = {
    "X-USER-TOKEN": TOKEN
}

# today = datetime.now()
today = datetime(year=2022, month=11, day=5)

post_pixel_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How may hours did you study python: ")
}

# response = requests.post(url=PIXELA_USER_API, json=parameters)
# print(response.text)
#
# response = requests.post(url=GRAPH_ENDPT, json=graph_config, headers=user_header)
# print(response.text)
# response = requests.delete(url=PIXEL_POST_ENDPT, headers=user_header)
# print(response.text)

response = requests.post(url=PIXEL_POST_ENDPT, json=post_pixel_body, headers=user_header)
print(response.text)

