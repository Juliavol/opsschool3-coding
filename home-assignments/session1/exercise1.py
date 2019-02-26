#!/user/bin/env python3
# -*- coding: UTF-8 -*-

"""Please write a program that does the following:
Read an input parameter with a JSON file name (for instance my_list.json)
The JSON will be in the following format (see below)

 Dictionary that will contain one nested hash and one list
 the hash will be of pairs of names and ages (name will be the key and age will be the value)
 the array will be a list of ages

Usage:
	python exercise1.py
"""
import codecs
import json
import os
import yaml
from pprint import pprint as pp


# Read an input parameter with a JSON file name
# C:\Users\julia.shub\PycharmProjects\OpsSchool\Session1-HW\opsschool3-coding\home-assignments\session1\my_list.json
def get_json():
    file_name = os.path.join(input('JSON full path: '))
    with open(file_name, encoding='UTF-8') as f:
        data = json.load(f)
    return data


def parse_json(json_data):
    '''the program will go over the list of people and divide them to buckets based on their ages + bonus bucket for people that are not in the range defined by the array in the json file

    Args:
         json_data: json_data is a dictionary imported from a file
    '''

    buckets_arr = json_data['buckets']
    ppl_ages_dict = json_data['ppl_ages']
    range_cur_item = {'People': []}
    start = True
    next_item = 0
    ranges = []
    rest_of_ppl = []

    buckets_arr = sorted(buckets_arr)
    #create bucket_ranges dictionaries
    for i in buckets_arr:
        if start:
            range_cur_item['Start'] = i
            start = False
        elif next_item >0:
            range_cur_item['Start'] = next_item
            range_cur_item['End'] = i -1
            next_item = i
            ranges.append(range_cur_item)
            range_cur_item = {'People': []}
        else:
            range_cur_item['End'] = i-1
            next_item = i
            ranges.append(range_cur_item)
            range_cur_item = {'People': []}
    #divide people into previously created buckets
    for name, age in ppl_ages_dict.items():
        found = False
        for age_range in ranges:
            if age_range['Start'] <= age <= age_range['End']:
                age_range['People'].append(name)
                found = True
        if not found:
            rest_of_ppl.append(name)
    #export names in buckets to yaml
    with codecs.open("my_list.yaml", "w", "utf-8") as write_file:
        for age_range in ranges:
            yaml.dump({"{0}-{1}".format(age_range['Start'], age_range['End']): age_range['People']}, write_file, default_flow_style=False, allow_unicode=True)
        yaml.dump({'rest_of_people': rest_of_ppl}, write_file, default_flow_style=False, allow_unicode=True)


def main():
    """Gets a JSON file, parses it, manipulates data and saves to YAML 
    """
    parse_json(get_json())

if __name__ == '__main__':
    main()  # the 0th arg is the module filename