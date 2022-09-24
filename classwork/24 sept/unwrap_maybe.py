# Create “unwrap_maybe” function. It should take as first argument - list, for example [1, 2], and as second - index,
# for example 3. If index didn’t exist in list, instead of exception - return a None object.

def unwrap_maybe(the_list, index):
    try:
        return the_list[index]
    except IndexError:
        return None


my_list = [1, 3, 4, 66, 7, 88, 4, 1]

print(unwrap_maybe(my_list, 33))
