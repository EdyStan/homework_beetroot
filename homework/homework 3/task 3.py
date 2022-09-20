my_name = 'eduard'
mhm = True

while mhm:
    name_my = input('Type my name pls: ')
    if name_my.lower() == my_name:
        print('Yep, that\'s my name. :*')
        mhm = False
    else:
        print('No :( What if you try again and type it well?')
