import json

infile = open('person.json','r')
data = json.load(infile)
print data['name']
infile.close()
