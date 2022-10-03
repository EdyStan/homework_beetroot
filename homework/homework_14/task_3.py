def arg_rules(type_, max_length: int, contains: list):
    def inside_func_1(func):
        def inside_func_2(name):
            if type(name) == type_ and len(name) < max_length:
                for content in contains:
                    if content not in name:
                        return False
                return func(name)
            else:
                return False

        return inside_func_2

    return inside_func_1


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
