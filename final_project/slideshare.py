from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import subprocess
import operator
import json

with open('creds.json', 'r') as infile:
    creds = json.load(infile)

driver = webdriver.Chrome()
# driver.get('https://slideshare.net')
# driver.execute_script('''document.querySelector('#nav-search-query').value='AI';''')

def slidepull(iteration):
    iter = str(iteration)
    driver.get('https://slideshare.net/explore')
    topics = driver.find_elements_by_css_selector(".title-link")
    random.choice(topics).click()
    time.sleep(1)

    decks = driver.find_elements_by_css_selector(".link-bg-img")
    random.choice(decks).click()
    time.sleep(1)

    try:
        if iteration == 0:
            slide = driver.find_element_by_css_selector(".slide_image")
        else:
            clips = driver.execute_script('''return slideshare_object.slideshow.clip_counts ;''')
            clips.pop('1')
            top_clip = max(clips.items(), key=operator.itemgetter(1))[0]

            slides = driver.find_elements_by_css_selector(".slide_image")
            top_clip = int(top_clip)
            top_clip_position = top_clip - 1

            slide = slides[top_clip_position]
            try:
                for i in range(0, top_clip_position):
                    time.sleep(.3)
                    driver.find_element_by_css_selector(".j-next-btn").click()
            except Exception as e:
                # print(e)
                pass

        slide_url = slide.get_attribute('data-full')
        return(slide_url)
    except Exception as e:
        # print(e)
        pass




    #     subprocess.call(["wget",slide_url,"-O","slides/slide"+iter+".jpg"])


slide_urls = []

# for i in range(0,2):
#     the_slide = slidepull(i)
#     print(the_slide)
#     if the_slide == None:
#         pass
#     else:
#         slide_urls.append(the_slide)
#     print(slide_urls)

def login():
    driver.get('https://docs.google.com/presentation/')
    time.sleep(1.9)
    driver.find_element_by_name('identifier').send_keys(creds['email_username'])
    time.sleep(1)
    driver.find_element_by_css_selector('#identifierNext').click()
    time.sleep(1.2)
    driver.find_element_by_name('password').send_keys(creds['email_password'])
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(Keys.RETURN)
    time.sleep(3)
    driver.find_element_by_css_selector('.docs-homescreen-templates-templateview-preview').click()
    project_id = driver.current_url.split('/')[5]
    return project_id

login()


# driver.quit()



    # clips = driver.find_elements_by_css_selector(".clipping-indicator")
    # if len(clips)>0:
    #     random.choice(clips).click()
    #     time.sleep(4)
    #     slide = driver.find_elements_by_css_selector(".slide_image")[1]
