from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Create a new Chrome session
driver = webdriver.Chrome(options)
driver.get('https://www.booking.com')
time.sleep(6)

try:
    close_button = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss sign in information.']")
except:
    pass
else:
    close_button.click()


search = driver.find_element(By.NAME, value="ss")
search.send_keys("Casablanca")
time.sleep(2)

search_button = driver.find_element(By.CSS_SELECTOR, "#indexsearch > div.hero-banner-searchbox > div > form > div.ffb9c3d6a3.c9a7790c31.e691439f9a > div.e22b782521.d12ff5f5bf > button")
search_button.click()

div_elements = driver.find_elements(By.CLASS_NAME, "c82435a4b8")

data_dic = {}
for div in div_elements[0:-2]:
    title = div.text.split("\n")[0]
    anchor_element = div.find_element(By.XPATH, "//a[@data-testid='property-card-desktop-single-image']")
    url = anchor_element.get_attribute("href")
    data_dic[title] = url    

with open("data.json", "w") as file:
    json.dump(data_dic, file, indent=4)
    
driver.quit()
