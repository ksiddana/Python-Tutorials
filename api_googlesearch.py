#!/usr/bin/python

import urllib2
import urllib
import json
import sys, os


def displayGoogleSearch(mySearch):
    
    file = open("api_googlesearch.html", "a")
    query = urllib.urlencode({'q':mySearch})
    url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"
    #query = urllib.urlencode({'gl':query})
    response = urllib2.urlopen(url + query)
    results = json.load(response)
    #results = data['responseData']['results']
    data = results['responseData']
    print 'Total results: %s' % data['cursor']['estimatedResultCount']
    file.write(str("\n" + 'Total results: %s' % data['cursor']['estimatedResultCount']))
    
    hits = data['results']
    print 'Top %d hits:' % len(hits)
    for h in hits:
        print ' ', h['url']
        file.write(str(h['url'] + "\n"))
    print 'For more results, see %s' % data['cursor']['moreResultsUrl']
    file.write(data['cursor']['moreResultsUrl'])
    file.close()
#nextResults = data['responseData']['cursor']['moreResultsUrl']

#    for result in results:
#        title = result['title']
#        url = result['url']
#        #file_object(url)
#        print ( title + '; ' + url)
#
#    print nextResults
#
#    print "See More Results: y/n"
#
#    if (raw_input() == 'y' or raw_input() == 'Y'):
#        response = urllib2.urlopen(nextResults)
#        data = json.load(response)
#        results = data['responseData']['results']
#
#        for result in results:
#            title = result['title']
#            url = result['url']
#            #file_object(url)
#            print ( title + '; ' + url)

mySearch = raw_input("What do you want to search for ? >> ")
displayGoogleSearch(mySearch)

