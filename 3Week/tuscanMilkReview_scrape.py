import requests
import json
import time
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/Tuscan-Dairy-Whole-Vitamin-Gallon/product-reviews/B00032G1S0/ref=sr_1_3_a_it'

my_params = {
    'ie': 'UTF8',
    'pageNumber': 1,
    'reviewerType': 'all_reviews'
}

def get_page(pagenumber):
    my_params = {
        'ie': 'UTF8',
        'pageNumber': pagenumber,
        'reviewerType': 'all_reviews'
    }
    html = requests.get(url, params = my_params).text
    soup = BeautifulSoup(html,'html.parser')
    reviews = soup.select('.review')
    output = []

    for review in reviews:
        print "got a review"
        title = review.select('.review-title')[0].text
        stars = review.select('.review-rating span')[0].text
        stars = float(stars.replace(" out of 5 stars", ""))
        reviewText = review.select('.review-text')[0].text

        item = {
            'title': title,
            'rating': stars,
            'body': reviewText
        }
        output.append(item)
        # print title, stars, reviewText
    return output

all_reviews = []
for i in range(1,191):
    try:
        some_reviews = get_page(i)
        all_reviews = all_reviews + some_reviews
        time.sleep(1)
    except:
        continue

outfile = open('reviews.json','w')
json.dump(all_reviews, outfile, indent=2)
outfile.close
