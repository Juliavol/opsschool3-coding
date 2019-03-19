#!/user/bin/env python3
# -*- coding: UTF-8 -*-

from weather import Weather, Unit
import requests
import sys
from requests import get
import json

API_KEY = 'a5b74bcd1a10b3ee324a0bf25c1b247d'

def get_weather_by_city(city):

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, API_KEY)
    r = requests.get(url)
    response_list = r.json()
    weather = response_list['weather'][0]

    temp = response_list['main']['temp']
    print('The weather in {}, is {} degrees'.format(city,  temp))


def main(city):
    get_weather_by_city(city)


if __name__ == '__main__':
    main(sys.argv[1])




