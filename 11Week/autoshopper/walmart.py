from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
driver = webdriver.Chrome()

def go_shopping():
    driver.get('https://walmart.com')
    searchbar = driver.find_element_by_css_selector("#global-search-input")
    letters = 'abcdefghijklmnopqrstuvwxyz'

    random.choice(letters)
    query = random.choice(letters) + random.choice(letters)
    searchbar.send_keys(query)

    time.sleep(1)
    options = driver.find_elements_by_css_selector('.typeahead-row-link')
    random.choice(options).click()

    time.sleep(1)

    products = driver.find_elements_by_css_selector('.search-result-productimage')
    random.choice(products).click()

    time.sleep(1)
    driver.find_element_by_css_selector('.prod-ProductCTA--primary').click()
    time.sleep(3)

def login():
    driver.get('https://walmart.com/account/login')
    time.sleep(1)
    driver.find_element_by_name('email').send_keys('lavigne@nyu.edu')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('detourning')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(Keys.RETURN)

login()

for i in range(0,100):
    try:
        go_shopping()
    except Exception as e:
        print(e)


#driver.quit()
