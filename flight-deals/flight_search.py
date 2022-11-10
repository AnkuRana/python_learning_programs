import requests
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.KIWI_API = os.environ.get("KIWI_API")
        self.KIWI_KEY = os.environ.get("KIWI_KEY")
        self.query = {}
        self.header = {
            "apikey": self.KIWI_KEY,
            "accept": "application/json"
        }
        self.date_from = datetime.now().strftime("%d/%m/%Y")
        self.date_to = (datetime.now() + relativedelta(months=+6)).strftime("%d/%m/%Y")

    def make_query_list(self, city_list):
        cities = ""
        for n in range(0, len(city_list)):
            cities += city_list[n] + ","
        cities = cities.rstrip(",")
        print(cities)
        self.query = {
                "fly_from": "DEL",
                "fly_to": cities,
                "date_from": self.date_from,
                "date_to": self.date_to,
                "flight_type": "oneway",
                "curr": "INR"
            }

    def get_flight_data(self):
        response_flights = requests.get(url=self.KIWI_API, headers=self.header, params=self.query)
        response_flights.raise_for_status()
        print(response_flights.json())
