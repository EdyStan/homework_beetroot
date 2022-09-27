import json

with open('phone_book.json') as outfile:
    list_obj = json.load(outfile)

list_obj[0]["last_name"] = "Duck"
list_obj[0]["telephone_number"] = "011258393"

if input("Are there too many Peppa Pigs?(y/n)\n") == 'y':
    try:
        del list_obj[1]
    except IndexError:
        print('There are no Peppa Pigs.')

with open('phone_book.json', 'w') as jsonfile:
    json.dump(list_obj, jsonfile, indent=4)
