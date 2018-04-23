"""
Shows basic usage of the Slides API. Prints the number of slides and elments in
a presentation.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Setup the Slides API
SCOPES = 'https://www.googleapis.com/auth/presentations'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('slides', 'v1', http=creds.authorize(Http()))

# Call the Slides API
PRESENTATION_ID = '1dCx4leIpkSv--M8FfcM7g4c7SH6YDvIi-Vr9cGzS4HE'
presentation = service.presentations().get(presentationId=PRESENTATION_ID).execute()
slides = presentation.get('slides')
title_id = slides[0].get('pageElements')[0]['objectId']
subtitle_id = slides[0].get('pageElements')[1]['objectId']
print(slides[1].get('slideProperties')['notesPage']['notesProperties']['speakerNotesObjectId'])
# ['speakerNotesObjectId']
print(title_id)
print(subtitle_id)

def change_title():
    requests = [
        {
            "insertText": {
                "objectId": title_id,
                "text": "Good Talk",
                "insertionIndex": 0
            }
        }
     ]

    body = {
            'requests': requests
    }

    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()
# change_title()

notes_id = slides[1].get('slideProperties')['notesPage']['notesProperties']['speakerNotesObjectId']

def notes_update(the_slides, iteration):
    notes_id = the_slides[i].get('slideProperties')['notesPage']['notesProperties']['speakerNotesObjectId']
    requests = [
        {
            "insertText": {
                "objectId": notes_id,
                "text": "hi"}
        }
     ]

    body = {
            'requests': requests
    }
    response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
                                                          body=body).execute()

slides = presentation.get('slides')
for i in range(len(slides)):
    notes_update(slides, i)

print ('The presentation contains {} slides:'.format(len(slides)))
# for i, slide in enumerate(slides):
#     print('- Slide #{} contains {} elements.'.format(i + 1,
#                                                      len(slide.get('pageElements'))))
#
# requests = [
#     {
#         'createSlide': {
#             'objectId': '3424234234230904317031275981435-4841-',
#             'insertionIndex': '1'
#         }
#     }
# ]
#
# body = {
#     'requests': requests
# }
#
# response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
#                                                       body=body).execute()
# create_slide_response = response.get('replies')[0].get('createSlide')
# print('Created slide with ID: {0}'.format(create_slide_response.get('objectId')))
#
# requests = [
#     {
#         "updatePageProperties": {
#             "objectId": '3424234234230904317031275981435-4841-',
#             "pageProperties": {
#                 "pageBackgroundFill": {
#                     "stretchedPictureFill": {
#                     "contentUrl": 'https://image.slidesharecdn.com/webinarhowtoscaleadreamsalesteam-160210174334/95/webinar-how-to-scale-a-dream-sales-team-4-1024.jpg?cb=1455214873'
#                     }
#                 }
#             },
#             "fields": "pageBackgroundFill"
#         }
#     }
# ]
#
# body = {
#     'requests': requests
# }
#
#
# response = service.presentations().batchUpdate(presentationId=PRESENTATION_ID,
#                                                       body=body).execute()
