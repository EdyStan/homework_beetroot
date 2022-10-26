# Write a program which will use regex to recognize is inputted by user number - have a correct format. References:
# +420 777 803 999, +1 203 532 345
# If number is correct - print ("Good Number!"). If not - print "Wrong number format!"
# Addition - modify this program to catch, was in a user input some number. If yes - parse it and print in output.
# If no - print "There is no number".

from re import fullmatch, findall

somethin = "\+[0-9]{1,3}\s\d{3}\s\d{3}\s\d{3}"
print(fullmatch(somethin, input("\nInput some phone number: ")))

if fullmatch(somethin, input('2nd input: ')):
    print('It works!')
else:
    print('It doesn\'t work!')


#2nd part

somethin_2 = findall("\+[0-9]{1,3}\s\d{3}\s\d{3}\s\d{3}", input('Input 3: '))

print(somethin_2)

if somethin_2:
    print(set(somethin_2))
else:
    print('No number :(')
