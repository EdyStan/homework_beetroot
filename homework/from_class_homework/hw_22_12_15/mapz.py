import requests
import urllib.parse

the_key = ''
base_url = ' https://maps.googleapis.com/maps/api/geocode/json'

unfiltered_input = input('Please, write the address:\n')

safe_url = urllib.parse.quote(unfiltered_input)

full_url = base_url + f"?address={safe_url}&key={the_key}"

r = requests.get(full_url)


def recursive_search_for_location(dict_object):
    for key, value in dict_object:
        if key == 'location':
            return value
        elif type(value) == dict:
            potential_final_location = recursive_search_for_location(value)
            if potential_final_location is not None:
                return potential_final_location
