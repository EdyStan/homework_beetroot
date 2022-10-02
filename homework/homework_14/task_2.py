def stop_words(words: list):
    def inside_func_1(func):
        def inside_func_2(name):
            sequence = func(name)
            for word in words:
                if word in sequence:
                    sequence = sequence.replace(word, '*')
            return sequence

        return inside_func_2

    return inside_func_1


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
