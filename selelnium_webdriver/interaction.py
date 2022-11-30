from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# webDr_path = "X:/Entertainment/study/ComputerScience/chrome_driver/chromedriver.exe"

driver = webdriver.Chrome()
wiki_url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(wiki_url)
# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(article_count.text)
search = driver.find_element(By.NAME, "search")
search.send_keys("python")
search.send_keys(Keys.ENTER)
driver.quit()
