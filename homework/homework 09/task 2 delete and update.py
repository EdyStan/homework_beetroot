import json

with open('phone_book.json') as outfile:
    list_obj = json.load(outfile)

list_obj[0]["last_name"] = "Goose"
list_obj[1]["telephone_number"] = "055339476"
del list_obj[0]["telephone_number"]

with open('phone_book.json', 'w') as jsonfile:
    json.dump(list_obj, jsonfile, indent=4)
