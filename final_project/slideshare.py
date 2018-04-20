## import google api modules
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
# scraping modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import subprocess
import operator

# import google slides credentials
import json

with open('creds.json', 'r') as infile:
    creds = json.load(infile)

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)
print(driver.get_window_size())
driver.set_window_size(1440,900)
print(driver.get_window_size())
# driver.get('https://slideshare.net')
# driver.execute_script('''document.querySelector('#nav-search-query').value='AI';''')

## the two driver functions, slidepull and login
# slidepull downloads popular slides from slideshare
# login logs into google slides and opens up a blank slidedeck, returning the slidedeck ID

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
        # subprocess.call(["wget",slide_url,"-O","slides/slide"+iter+".jpg"])
        return(slide_url)
    except Exception as e:
        # print(e)
        pass



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






## driver behavior

#scraping
slide_urls = []

for i in range(0,10):
    the_slide = slidepull(i)
    print(the_slide)
    if the_slide == None:
        pass
    else:
        slide_urls.append(the_slide)
    print(slide_urls)

login()

project_id = driver.current_url.split('/')[5]
first_slide_id = driver.current_url.split('/')[6].split('.')[1]

## Setup the Slides API
SCOPES = 'https://www.googleapis.com/auth/presentations'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('slides', 'v1', http=creds.authorize(Http()))

# login to google slides and call the Slides API
PRESENTATION_ID = project_id
presentation = service.presentations().get(presentationId=PRESENTATION_ID).execute()
slides = presentation.get('slides')
title_id = slides[0].get('pageElements')[0]['objectId']
subtitle_id = slides[0].get('pageElements')[1]['objectId']

def deck_populate(slide_ID, iteration):
    requests = [
        {
            'createSlide': {
                'objectId': slide_ID,
                'insertionIndex': '1'
            }
        }
    ]

    body = {
        'requests': requests
    }

    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()
    create_slide_response = response.get('replies')[0].get('createSlide')
    print('Created slide with ID: {0}'.format(create_slide_response.get('objectId')))

    requests = [
        {
            "updatePageProperties": {
                "objectId": slide_ID,
                "pageProperties": {
                    "pageBackgroundFill": {
                        "stretchedPictureFill": {
                        "contentUrl": slide_urls[len(slide_urls)-1-iteration]
                        }
                    }
                },
                "fields": "pageBackgroundFill"
            }
        }
    ]

    body = {
        'requests': requests
    }


    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()

for i in range(0, len(slide_urls)):
    unique_id = random.randint(1000,10000000000000000000000)
    unique_id = str(unique_id)
    deck_populate(unique_id,i)


def change_title():
    requests = [
        {
            "insertText": {
                "objectId": title_id,
                "text": "WELCOME TO",
                "insertionIndex": 0
            }
        }
     ]

    body = {
            'requests': requests
    }

    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()

    time.sleep(4)
    requests = [
        {
            "insertText": {
                "objectId": subtitle_id,
                "text": "GOOD CONFERENCE TALK",
                "insertionIndex": 0
            }
        }
     ]

    body = {
            'requests': requests
    }

    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()

change_title()
time.sleep(1)
driver.find_element_by_css_selector("#punch-start-presentation-left").click()


# driver.quit()



    # clips = driver.find_elements_by_css_selector(".clipping-indicator")
    # if len(clips)>0:
    #     random.choice(clips).click()
    #     time.sleep(4)
    #     slide = driver.find_elements_by_css_selector(".slide_image")[1]
