from task_2_classes import Author, Book, Library

# initializing the classes
a1 = Author('Shakespeare', 'England', 'April 1564')
a2 = Author('Agatha Christie', 'United Kingdom', 'Sep 1890')
b1 = Book('Hamlet', 1601, a1)
b2 = Book('Romeo and Juliet', 1595, a1)
b3 = Book('Death on the Nile', 1937, a2)
b4 = Book('Five little pigs', 1942, a2)

# adding books to the author's bibliography
a1.new_book(b1)
a1.new_book(b2)
a2.new_book(b3)
a2.new_book(b4)

# testing the books
print('Books:')
print(b1)
print(b2)
print(b3)
print(b4)
print(b4.count_books)
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
l1 = Library('Vatican Library')
l1.new_book('Hamlet', 1601, a1)
l1.new_book('Death on the Nile', 1937, a2)

# testing the library
print('\nTesting library 1:')
print(l1.authors)
print(l1.books)
l1.group_by_year(1601)
l1.group_by_author(a1)

l1.group_by_author(a2)
