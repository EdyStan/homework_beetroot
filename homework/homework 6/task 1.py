"""
Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and
the number of occurrences as values.
"""

sentence = input('Pls write a sentence: ')
i = 0
words = ['']
the_dictionary = {}

for character in sentence:
    if character == ' ':
        i += 1
        words.append('')
    else:
        words[i] += character

print(words)

for index in range(len(words)):
    if words[index] not in the_dictionary:
        the_dictionary[words[index]] = 1
    else:
        the_dictionary[words[index]] += 1

print(the_dictionary)
