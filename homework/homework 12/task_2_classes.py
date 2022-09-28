class Book:

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f'{self.name} ({self.year}) by {self.author}'

    def __str__(self):
        return f'{self.name} ({self.year}) by {self.author}'


class Author:

    def __init__(self, name, country, birthday, *books):
        self.books = []
        for book in books:
            self.books.append(book)
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'


class Library:

    def __init__(self, name, books=None, authors=None):
        if books is None:
            books = []
        if authors is None:
            authors = set()
        self.name = name
        self.books = books
        self.authors = authors

    def __repr__(self):
        return f'{self.name} Library'

    def __str__(self):
        return f'{self.name} Library'

    def new_book(self, name: str, year: int, author: Author):
        for book in author.books:
            if book.name == name and book.year == year:
                self.books.append(book)
                self.authors.add(author)

    def group_by_author(self, author: Author):
        print(f'Books writen by {author}:')
        for book in self.books:
            if book.author.name == author.name:
                print(book)

    def group_by_year(self, year: int):
        print(f'Books writen in {year}:')
        for book in self.books:
            if book.year == year:
                print(book)
