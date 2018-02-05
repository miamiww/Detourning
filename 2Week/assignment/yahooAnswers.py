import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys
import unittest
import re


# url = "https://answers.yahoo.com/"
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html,"html.parser")
#
# questions = soup.select('.title')
# output = []
# for question in questions:
#     clean_question = question.text.strip().encode('utf-8')
#     output.append(clean_question)
#
# print output

browser = webdriver.Chrome()

browser.get("https://answers.yahoo.com/")
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 500

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

post_elems = browser.find_elements_by_class_name("title")

for post in post_elems:
    print post.text.strip().encode('utf-8')

# class Sel(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(30)
#         self.base_url = "https://answers.yahoo.com/"
#         self.verificationErrors = []
#         self.accept_next_alert = True
#     def test_sel(self):
#         driver = self.driver
#         delay = 1
#         driver.get(self.base_url)
#         driver.find_element_by_link_text(".title").click()
#         for i in range(1,100):
#             self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(4)
#         html_source = driver.page_source
#         data = html_source.encode('utf-8')
#         print data
#
#
# if __name__ == "__main__":
#     unittest.main()
