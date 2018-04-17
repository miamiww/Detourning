from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import subprocess
driver = webdriver.Chrome()

# driver.get('https://slideshare.net')
# driver.execute_script('''document.querySelector('#nav-search-query').value='AI';''')

def slidepull(iteration):
    iter = str(iteration)
    driver.get('https://slideshare.net/explore')
    topics = driver.find_elements_by_css_selector(".title-link")
    random.choice(topics).click()
    time.sleep(2)

    decks = driver.find_elements_by_css_selector(".link-bg-img")
    random.choice(decks).click()
    time.sleep(2)

    clips = driver.find_elements_by_css_selector(".clipping-indicator")
    if len(clips)>0:
        random.choice(clips).click()
        time.sleep(2)
        slide = driver.find_element_by_css_selector(".slide_image")
        slide_url = slide.get_attribute('src')
        print(slide_url)

        subprocess.call(["wget",slide_url,"-O","slides/slide"+iter+".jpg"])

for i in range(0,15):
    slidepull(i)

driver.quit()
