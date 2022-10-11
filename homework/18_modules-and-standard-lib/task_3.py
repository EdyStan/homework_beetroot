def count_lines(file_name):
    with open(file_name, 'r') as os_file:
        os_file = os_file.readlines()
    return len(os_file)


def count_chars(file_name):
    with open(file_name, 'r') as os_file:
        os_file = os_file.read()
    return len(os_file)


def test(file_name):
    return 'Lines: ' + str(count_lines(file_name)) + '\nChars: ' + str(count_chars(file_name))


print(test('task_3.py'))
