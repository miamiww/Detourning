import io
import requests
import pytesseract
from PIL import Image
response = requests.get("https://image.slidesharecdn.com/the-cx-paradox-3-ways-measuring-your-customer-satisfaction-could-actually-damage-it-151104184431-lva1-app6891/95/the-cx-paradox-3-ways-measuring-your-customer-satisfaction-could-actually-damage-it-5-1024.jpg?cb=1446750215")
# print( type(response) ) # <class 'requests.models.Response'>
img = Image.open(io.BytesIO(response.content))
# print( type(img) ) # <class 'PIL.JpegImagePlugin.JpegImageFile'>
text = pytesseract.image_to_string(img)
print( text )
