#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager
from flight_search import FlightSearch

data = data_manager.DataManager()
city_details = data.get_city_code()
iatacodes = []


for n in range(0, len(city_details)):
    iatacodes.append(city_details[n]["iataCode"])

flight_search = FlightSearch()
flight_search.make_query_list(iatacodes)
flight_search.get_flight_data()
