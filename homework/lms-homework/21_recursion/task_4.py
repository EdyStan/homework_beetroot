def reverse(input_str):
    if len(input_str) == 0:
        return ''
    return input_str[-1] + reverse(input_str[:-1])


print(reverse('Roses are red, violets are  blue'))
