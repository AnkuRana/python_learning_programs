import requests
import os


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_API = os.environ.get("SHEETY_API")
        self.SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
        self.headers = {
            "Authorization": self.SHEETY_TOKEN
        }

    def get_city_code(self):
        """ return list of Cities where you want to fly to"""
        repsonse_city = requests.get(url=self.SHEETY_API, headers=self.headers,)
        repsonse_city.raise_for_status()
        return repsonse_city.json()["prices"]
