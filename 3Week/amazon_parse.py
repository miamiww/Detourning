import json
from textblob import TextBlob

infile = open('reviews.json', 'r')
reviews = json.load(infile)

all_adjectives = {}
# total_stars = 0
for review in reviews:
    blob = TextBlob(review['body'])
    for tag in blob.tags:
        if tag[1] == 'JJ':
            word = tag[0].encode('UTF8')
            if word in all_adjectives:
                all_adjectives[word] += 1
            else:
                all_adjectives[word] = 1

    # total_stars = total_stars + review['rating']
# print total_stars / len(reviews)
print all_adjectives
infile.close()
