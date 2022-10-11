import json


def add_entry():
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


def delete_and_update():
    with open('phone_book.json') as outfile:
        list_obj = json.load(outfile)

    list_obj[0]["last_name"] = "Goose"
    list_obj[1]["telephone_number"] = "055339476"
    del list_obj[0]["telephone_number"]

    with open('phone_book.json', 'w') as jsonfile:
        json.dump(list_obj, jsonfile, indent=4)

    jsonfile.close()


def recover_initial():
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
