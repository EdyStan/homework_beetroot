def oops():
    raise KeyError


try:
    oops()
except KeyError:
    print('dddd')


