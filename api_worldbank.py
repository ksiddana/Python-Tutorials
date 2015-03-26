#!/usr/bin/python

import urllib2
import json

"""http://climatedataapi.worldbank.org/climateweb/rest/v1/country/type/var/start/end/ISO3[.ext]
"""

def climate_data_search(country):
    #api_key = locu_api
    
    #mavg, annualavg, manom, annualnom
    type = "annualavg"
    
    #pr = precipiation (rainfall and assumed water equivalent), in millimeters
    var = "pr"
    start = "1990"
    end = "2015"
    country_code_iso3 = country
    url = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country'
    #final_url = url + '/' + type
    final_url = url + '/' + type + '/' + var + '/' + start + '/' + end + '/' + country_code_iso3 + ".json"
    #final_url = 'https://ismaelc-pinterest.p.mashape.com/jwmoz/boards'
    print final_url
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    print data

climate_data_search("bra")