def which_function(func_name):
    if func_name == 'addition':
        def addition():
            a = int(input('\' \' + \' \' = ?\n'))
            b = int(input(f'{a} + \' \' = ?\n'))
            print(f'{a} + {b} = {a + b}')
        return addition()
    elif func_name == 'subtraction':
        def subtraction():
            a = int(input('\' \' - \' \' = ?\n'))
            b = int(input(f'{a} - \' \' = ?\n'))
            print(f'{a} - {b} = {a - b}')
        return subtraction()


which_function('addition')
which_function('subtraction')
