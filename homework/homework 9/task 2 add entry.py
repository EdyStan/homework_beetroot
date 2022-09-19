import json

pp = {'first_name': 'Peppa',
      'last_name': 'Pig',
      'full name': 'Peppa Pig',
      'telephone_number': '011256973',
      'city/state': 'Oklahoma'}

with open('phone_book.json') as outfile:
    list_obj = json.load(outfile)

list_obj.append(pp)

with open('phone_book.json', 'w') as jsonfile:
    json.dump(list_obj, jsonfile, indent=4)
