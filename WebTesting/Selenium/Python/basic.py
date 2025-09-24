from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = "/home/steve/Documents/projects/WebTesting/Selenium/Python/chrome-linux64/chrome"

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.bbc.co.uk/search?d=HOMEPAGE_PS')
time.sleep(5)
# search_box = driver.find_element_by_name('q')
search_box = driver.find_element(By.ID,'searchInput')
search_box.send_keys('tennis ranking')
search_button = driver.find_element(By.ID,'searchButton')
search_button.click()
time.sleep(5)
driver.quit()