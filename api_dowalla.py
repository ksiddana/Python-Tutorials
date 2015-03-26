#!/usr/bin/python

import urllib2
import json

locu_api = ''

def locu_search(query):
    api_key = locu_api
    url = 'https' + api_key
    final_url = url "?"
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)

    