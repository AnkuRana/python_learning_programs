from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
store = driver.find_element(By.ID, "store")
store_items = store.find_elements(By.TAG_NAME, "div")
store_dic = {}

for i in range(0, len(store_items)-1):
    item_name = store_items[i].get_property("id")
    item_cost = store_items[i].text.split("-")[1].split("\n")[0].lstrip()
    if "," in item_cost:
        item_cost = store_items[i].text.split("-")[1].split("\n")[0].lstrip().split(",")
        item_cost = float("".join(item_cost))
    else:
        item_cost = float(item_cost)
    store_dic[item_name] = item_cost

# cost_list = store_dic.values()
# cost_list = cost_list.reverse()
# for i in range(0, len(store_items) - 2):
#     item_name = store_items[i].get_property("id")
#     item_cost = store_items[i].text.split("-")
#     item_cost = item_cost[1].split("\\")
#     item_cost = item_cost[0].lstrip()
#     store_dic = {item_name: item_cost}
# print(store_dic)
reversed_store_dic = {}
for key in reversed(store_dic):
    reversed_store_dic[key] = store_dic[key]

item_buy_count = {}

# initializing the dic with zero
for key in reversed_store_dic:
    item_buy_count[key] = 0

start = time.time()
while True:
    cookie.click()
    money = float("".join(driver.find_element(By.ID, "money").text.split(",")))
    for key in reversed_store_dic:
        if money > reversed_store_dic[key]:
            if item_buy_count[key] == 1:
                break
            buy_item = store.find_element(By.ID, f"{key}")
            buy_item.click()
            item_buy_count[key] = 1
            break
    end = time.time()
    time_lapses = end - start
    if time_lapses >= 300:
        print("time is up")
        break

print(driver.find_element(By.ID, "cps").text)
driver.quit()
