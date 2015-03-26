#from urllib2 import urlopen

# kittens = urlopen('http://placekitten.com/200/300')

# f = open('kittens.jpg', 'wb')
# f.write(kittens.read())
# f.close()

from urllib2 import urlopen
from pprint import pprint
from json import load 

#url = 'http://api.npr.org/query?apiKey=' 
url = 'http://api.rottentomatoes.com/api/public/v1.0.json?apikey=nud5sb3bqav9sywvxy2b8t37'
#key = 'API_KEY'
#url = url + key
#url += '&numResults=3&format=json&id='
#url += raw_input("Which NPR ID do you want to query?")

response = urlopen(url)
response = response.read()
#json_obj = load(response)

#print json_obj
print response

#for story in json_obj['list']['story']:
#	print story['title']['$text']