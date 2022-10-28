import json
from ..homework_09.task_2 import add_entry, recover_initial, delete_and_update


def add_entry_pp_testing():
    add_entry()
    with open('phone_book.json') as outfile:
        list_obj = json.load(outfile)
    assert list_obj == ''
    recover_initial()


def delete_and_update_testing():
    delete_and_update()
    with open('phone_book.json') as outfile:
        list_obj = json.load(outfile)
    assert list_obj == ''
    recover_initial()
