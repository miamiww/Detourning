from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
driver = webdriver.Chrome()

def go_shopping():
    driver.get('https://seamless.com')
    letters = 'abcdefghijklmnopqrstuvwxyz'

    driver.find_element_by_css_selector('.addressInput-textInput').click()
    time.sleep(1)
    driver.find_element_by_css_selector('.addressInput-textInput').send_keys('720 Broadway, New York')
    time.sleep(1)
    driver.find_element_by_css_selector('.ghs-searchInput').click()
    driver.find_element_by_css_selector('.ghs-searchInput').send_keys(random.choice(letters))
    driver.find_element_by_css_selector('.ghs-searchInput').send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_element_by_css_selector('.ghs-searchInput').click()
    time.sleep(3)

    options = driver.find_elements_by_css_selector('.s-list-item')
    random.choice(options).click()

    time.sleep(2)
    options = driver.find_elements_by_css_selector('.restaurant-name')
    if len(options) > 1:
        random.choice(options).click()

    for i in range(0,5):
        try:
            time.sleep(2)
            options = driver.find_elements_by_css_selector('.menuItem-inner')
            random.choice(options).click()
            time.sleep(2)

            menu_options = driver.find_elements_by_css_selector('.menuItemModal-choice')
            if len(menu_options) > 0:
                for menu_option in menu_options:
                    options = menu_option.find_elements_by_css_selector('.s-col-sm-4')
                    if len(options) > 0:
                        random.choice(options).click()

                time.sleep(2)
                driver.find_element_by_css_selector('menuItemModal-btnSubmit')
                time.sleep(2)
            else:
                driver.find_element_by_css_selector('menuItemModal-btnSubmit')
                time.sleep(2)
        except Exception as e:
            print(e)

def login():
    driver.get('https://seamless.com')
    driver.find_element_by_css_selector('button').click()
    time.sleep(3)
    driver.find_element_by_name('email').send_keys('lavigne+detourning@nyu.edu')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('detourning')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(Keys.RETURN)


login()
time.sleep(2)
go_shopping()
# driver.quit()
