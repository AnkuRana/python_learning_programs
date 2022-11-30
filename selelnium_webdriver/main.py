from selenium import webdriver
from selenium.webdriver.common.by import By

webDr_path = "X:/Entertainment/study/ComputerScience/chrome_driver/chromedriver.exe"

web_driver = webdriver.Chrome()
web_driver.get("https://www.python.org/")

list_times = web_driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
list_events = web_driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
dic_items = {}
for item in range(len(list_times)):
    dic_items[item] = {"time": list_times[item].text, "name": list_events[item].text}

print(dic_items)

web_driver.quit()

