phone_num = '0728116655'

if phone_num.isnumeric() is True and len(phone_num) == 10:
    print('This could be a phone number')
else:
    print('This can\'t be a phone number')
