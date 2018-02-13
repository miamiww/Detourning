from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://google.com')

searcher = driver.find_element_by_name('q')
searcher.send_keys("best cheeses")
searcher.send_keys(Keys.RETURN)
