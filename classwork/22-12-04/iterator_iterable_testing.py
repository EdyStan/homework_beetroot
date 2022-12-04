from iterator_iterable import ChristmasPresents

santa_sack = ChristmasPresents(['best mum mug', 'shirt'], ['best dad mug', 'world cup 2022 ball'],
                               ['Harry Potter pen', 'earrings'], ['earrings'])

# testing property
print(santa_sack.mum_presents)

# testing setter
santa_sack.sis_presents = 'cactus'
santa_sack.oana_presents = 'roses'

# testing deleter
print(santa_sack.oana_presents)
del santa_sack.oana_presents
print(santa_sack.oana_presents)

# testing class iteration
for present in santa_sack:
    print(present)
