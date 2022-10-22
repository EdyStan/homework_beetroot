def is_palindrome(looking_str: str):
    if looking_str == '':
        return True
    elif looking_str[0] == looking_str[-1]:
        return is_palindrome(looking_str[1:-1])
    else:
        return False


assert is_palindrome('earth') is False
assert is_palindrome('spaces') is False
assert is_palindrome('mum') is True
assert is_palindrome('a') is True
