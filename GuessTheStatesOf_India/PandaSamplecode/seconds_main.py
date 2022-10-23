import pandas
# data_list = []
# with open("weather_data.csv", mode="r") as file:
#     data_list = file.readlines()
#
# for i in range(0, len(data_list)):
#     data_list[i] = data_list[i].strip()
# import csv

# temperature = []

# with open("weather_data.csv", mode="r") as file:
#      data = csv.reader(file)
#      for row in data:
#          temperature.append(row[1])
#
# def conver_to_faren(temp_in_celcius):
#     temp = (9/5) * temp_in_celcius + 32
#     return temp

# data = pandas.read_csv("weather_data.csv")
# average = 0
# temperature = data["temp"].to_list()
# # print(temperature)
# average = data["temp"].mean()
# max = data["temp"].max()
# # print(data[data.temp == max])
#
# monday = data[data.day == "Monday"]
# # monday.temp.
# print((conver_to_faren(int(monday.temp))))

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(len(data[data["Primary Fur Color"] == "Gray"]))
# fur_color = data["Primary Fur Color"].tolist()
# colors = ["Gray", "Cinnamon", "Black"]
# count= []
# dic = {}
# for color in colors:
#     count.append(fur_color.count(color))
#
# dic["colors"] = colors
# dic["count"] = count
#
# data_to_frame = pandas.DataFrame(dic)
# data_to_frame.to_csv("central_park_squirrels.csv")