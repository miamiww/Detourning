from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=tongues")

def get_page():
    time.sleep(2)
    items = driver.find_elements_by_css_selector('h2.title')
    for item in items:
        print item.text
    driver.execute_script('document.querySelector("a.next").click()')
    get_page()

get_page()

driver.quit()
