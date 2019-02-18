#!/user/bin/env python3
# -*- coding: UTF-8 -*-

"""Please write a program that does the following:
Read an input parameter with a JSON file name (for instance my_list.json)
The JSON will be in the following format (see below)

 Dictionary that will contain one nested hash and one list
 the hash will be of pairs of names and ages (name will be the key and age will be the value)
 the array will be a list of ages

 note for Yaron - this excercise needs parsing to understand.
 The array is already contained withing the sample file, but the exercise is written as if it needs to be created.
 Also, this seems a bit much for people who had not touched python earliet than 2 weeks ago. it requires better wtitten
 questions, broken down to smaller pieces, or more time to do the homeworks since this is a lot of research for people who don't neccessarily know what they are looking for

Usage:
	python exercise1.py
"""
import codecs
import json
import os
import yaml
from pprint import pprint as pp


# Read an input parameter with a JSON file name
# ppl_ages_dict C:\Users\julia.shub\PycharmProjects\OpsSchool\Session1-HW\opsschool3-coding\home-assignments\session1\my_list.json
def get_json():
    file_name = os.path.join(input('JSON full path: '))
    with open(file_name, encoding='UTF-8') as f:
        data = json.load(f)
    return data


def parse_json(json_data):
    '''the program will go over the list of people and divide them to buckets based on their ages
    each bucket will hold all the names of the people with age between the partition key and the following partition key
    bucket  ‘20-25’ will hold a list of name that their age is between 20 and 25 (not including)
    this data will them be saved in a yaml format in a file with the same name as the input file with changed extension.
    bonus - if there is someone that doesn't fall into any of the baskets it will create a new bucket based on the oldest person and add all the people that fall into this bucket

    Args:
         json_data: json_data is a dictionary imported from a file
    '''

    buckets_arr = json_data['buckets']
    ppl_ages_dict = json_data['ppl_ages']
    range_cur_item = {
                'People': []
            }
    start = True
    next_item = 0
    ranges = []
    rest_of_ppl = []

    buckets_arr = sorted(buckets_arr)
    pp(ppl_ages_dict)
    print(buckets_arr)
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
            range_cur_item = {
                'People': []
            }
        else:
            range_cur_item['End'] = i-1
            next_item = i
            ranges.append(range_cur_item)
            range_cur_item = {
                'People': []
            }

    print(ranges)

    for name, age in ppl_ages_dict.items():
        found = False
        for age_range in ranges:
            if age_range['Start'] <= age <= age_range['End']:
                age_range['People'].append({name: age})
                found = True
        if not found:
            rest_of_ppl.append({name: age})

    with codecs.open("my_list.yaml", "w", "utf-8") as write_file:
        for age_range in ranges:
            yaml.dump({"{0}-{1}".format(age_range['Start'], age_range['End']): age_range['People']}, write_file)
        yaml.dump({'rest_of_people': rest_of_ppl}, write_file)


def main():
    """Gets a JSON file, parses it, manipulates data and saves to YAML
    """
    parse_json(get_json())

if __name__ == '__main__':
    main()  # the 0th arg is the module filename