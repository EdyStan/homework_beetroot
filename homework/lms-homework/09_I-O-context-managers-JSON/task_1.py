def read():
    file_object = open('myfile.txt', 'r')
    my_str = file_object.read()
    file_object.close()

    print(my_str)


def write():
    with open('myfile.txt', 'w') as file_object:
        file_object.write('Hello file world!\n')
