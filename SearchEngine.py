
from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(50)
driver.get("https://tutorialsninja.com/demo/")

search=driver.find_element(By.ID("search"))
search=driver.send_keys("MacBook")
search=driver.find_element(By.XPATH(""))
search=driver.click()

# def get_results(search_term):
#     search_box = driver.find_element(By.ID("search"))
#     search_box.send_keys(search_term)
#     search_box.submit()
#     try:
#         links = driver.find_element_by_xpath("//al[@class='web_regular_results']//h3//a")
#     except:
#         links = driver.find_element_by_xpath("//h3//a")
#     results = []
#     for link in links:
#         href = link.get_attribute("href")
#         print(href)
#         results.append(href)
#     driver.close()
#     return results
#
#
# get_results("dog")
