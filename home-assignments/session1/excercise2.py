#!/user/bin/env python3
# -*- coding: UTF-8 -*-

'''

1.
Write a python program, that checks your location according to your IP.
Then checks the current weather at your location and writes the result to a file in a regular text format.

2.
In that same program, create a list with at least 10 cities,
And print their current weather in the following format:
“The weather in <city>, <country>(full country name) is XX degrees.

'''

import sys
from urllib.request import urlopen
import requests
import json
import sys
import configparser

api_key = 'a5b74bcd1a10b3ee324a0bf25c1b247d'

def get_geo_by_ip():
    send_url = "http://api.ipstack.com/109.64.9.109?access_key=c755c7cae07cf8943a551ee0562b3825"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    lat = geo_json['latitude']
    lon = geo_json['longitude']
    city = geo_json['city']
    country = geo_json['country_name']

    location = [lat, lon, city, country]
    location_dict = {}
    print(lat)
    print(lon)
    print(city)
    print(country)

    return lat, lon


# sample api call - http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={}
def get_weather(api_key, lat, lon):
    url = "http://api.openweathermap.org/data/2.5/forecast?appid={}&lat={}&lon={}".format(api_key, lat, lon)
    r = requests.get(url)

    # Get weather data from response
    response_list = r.json()
    weather = response_list['list'][0]['weather']
    print(weather)

    # export list to file
    with open('cur_weather.txt', 'w') as f:
        for item in weather:
            f.write("%s\n" % item)
    return weather


def main():
    """Gets a JSON file, parses it, manipulates data and saves to YAML
    """
    lat, lon = get_geo_by_ip()
    get_weather(api_key, lat, lon)


if __name__ == '__main__':
    main()  # the 0th arg is the module filename
