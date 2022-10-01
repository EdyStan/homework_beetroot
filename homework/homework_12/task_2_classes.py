class Author:

    def __init__(self, name, country, birthday):
        self.books = []
        self.name = name
        self.country = country
        self.birthday = birthday

    def new_book(self, book):
        self.books.append(book)

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'


class Book:

    count_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.count_books += 1

    def __repr__(self):
        return f'{self.name} ({self.year}) by {self.author}'

    def __str__(self):
        return f'{self.name} ({self.year}) by {self.author}'


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self):
        return f'{self.name} Library'

    def __str__(self):
        return f'{self.name} Library'

    def new_book(self, name: str, year: int, author: Author):
        for book in author.books:
            if book.name == name and book.year == year:
                book.count_books += 1
                self.books.append(book)
                self.authors.append(author)

    def group_by_author(self, author: Author):
        print(f'Books writen by {author}:')
        for book in author.books:
            if book in self.books:
                print(book)

    def group_by_year(self, year: int):
        print(f'Books writen in {year}:')
        for book in self.books:
            if book.year == year:
                print(book)
