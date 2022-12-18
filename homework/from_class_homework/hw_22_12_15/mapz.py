import requests
import urllib.parse

the_key = ''
base_url = ' https://maps.googleapis.com/maps/api/geocode/json'

unfiltered_input = input('Please, write the address:\n')

safe_url = urllib.parse.quote(unfiltered_input)

full_url = base_url + f"?address={safe_url}&key={the_key}"

r = requests.get(full_url)

json_object = r.json()


print(json_object)
print(full_url)

print(json_object['results'][0]['geometry']['location'])