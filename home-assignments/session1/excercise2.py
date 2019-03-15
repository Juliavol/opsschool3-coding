#!/user/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import requests
import json

API_KEY = 'a5b74bcd1a10b3ee324a0bf25c1b247d'


def get_geo_by_ip():

    ip = requests.get('https://api.ipify.org').text
    send_url = "http://api.ipstack.com/{}?access_key=c755c7cae07cf8943a551ee0562b3825".format(ip)
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']

    return latitude, longitude


def get_weather_by_geo(API_KEY, lat, lon):

    url = "http://api.openweathermap.org/data/2.5/forecast?appid={}&lat={}&lon={}".format(API_KEY, lat, lon)
    r = requests.get(url)

    response_list = r.json()
    weather = response_list['list'][0]['weather']
    print(weather)

    with open('cur_weather.txt', 'w') as file:
        for item in weather:
            file.write("%s\n" % item)


def get_weather_by_city():

    cities = ['Moscow', 'Jerusalem', 'London', 'Dublin', 'Paris', 'Madrid', 'New Delhi', 'Los Angeles', 'Cairo', 'Santiago', 'Beijing']

    for city in cities:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, API_KEY)
        request = requests.get(url)
        response_list = request.json()
        country_code = response_list['sys']['country']
        weather = response_list['weather'][0]
        country = ''
        with open('country_name_ISO_3166_1.json') as json_file:
            json_data = json.load(json_file)
            for item in json_data:
                if item['Code'] == country_code:
                    country = item['Name']
                    break

        response_list = request.json()
        temp = response_list['main']['temp']

        print('The weather in {}, {} is {} degrees'.format(city, country, temp))


def main():

    lat, lon = get_geo_by_ip()
    get_weather_by_geo(API_KEY, lat, lon)
    get_weather_by_city()


if __name__ == '__main__':
    main()
