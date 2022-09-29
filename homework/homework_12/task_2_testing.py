import task_2_classes as t2

# initializing the variables
a1 = 'author'
b1 = t2.Book('Hamlet', 1601, a1)
b2 = t2.Book('Romeo and Juliet', 1595, a1)
a2 = 'author'
b3 = t2.Book('Death on the Nile', 1937, a2)
b4 = t2.Book('Five little pigs', 1942, a2)

# updating the variables cause this is the only way they will show what we want (hopefully)
a1 = t2.Author('Shakespeare', 'England', 'April 1564', b1, b2)
a2 = t2.Author('Agatha Christie', 'Sep 1890', b3, b4)
b1 = t2.Book('Hamlet', 1601, a1)
b2 = t2.Book('Romeo and Juliet', 1595, a1)
b3 = t2.Book('Death on the Nile', 1937, a2)
b4 = t2.Book('Five little pigs', 1942, a2)

# and let's update them once more

a1 = t2.Author('Shakespeare', 'England', 'April 1564', b1, b2)
a2 = t2.Author('Agatha Christie', 'Sep 1890', b3, b4)
b1 = t2.Book('Hamlet', 1601, a1)
b2 = t2.Book('Romeo and Juliet', 1595, a1)
b3 = t2.Book('Death on the Nile', 1937, a2)
b4 = t2.Book('Five little pigs', 1942, a2)

# testing the books
print('Books:')
print(b1)
print(b2)
print(b3)
print(b4)

# testing book 1
print('\nTesting book 1:')
print(b1.author.books)
print(b1.name)
print(b1.year)
print(b1.author)

# testing author 1
print('\nTesting author 1:')
print(a1)
print(a1.name)
print(a1.books)
print(a1.birthday)
print(a1.country)

# initializing and adding to library
l1 = t2.Library('Vatican Library')
l1.new_book('Hamlet', 1601, a1)
l1.new_book('Death on the Nile', 1937, a2)

# testing the library
print('\nTesting library 1:')
print(l1.authors)
print(l1.books)
l1.group_by_year(1601)
l1.group_by_author(a1)

l1.group_by_author(a2)  # but for some reason this doesn't work
print(b3.author.name)  # names for these two lines are the same
print(a2.name)  # but they don't execute the code in the class method idk why

# what didn't work?
# making a variable that increments with each creation of a book
# listing all the authors and all the books in library
# normally initializing the variables, without calling them twice
