import unittest
from ..homework_12.task_2_classes import Author, Book, Library


class AuthorBookLibTestCase(unittest.TestCase):
    def setUp(self):
        self.a1 = Author('Shakespeare', 'England', 'April 1564')
        self.a2 = Author('Agatha Christie', 'United Kingdom', 'Sep 1890')
        self.b1 = Book('Hamlet', 1601, self.a1)
        self.b2 = Book('Romeo and Juliet', 1595, self.a1)
        self.b3 = Book('Death on the Nile', 1937, self.a2)
        self.b4 = Book('Five little pigs', 1942, self.a2)
        self.l1 = Library('Vatican Library')
        self.a1.new_book(self.b1)
        self.a1.new_book(self.b2)
        self.a2.new_book(self.b3)
        self.a2.new_book(self.b4)
        self.l1.new_book('Hamlet', 1601, self.a1)
        self.l1.new_book('Romeo and Juliet', 1595, self.a1)
        self.l1.new_book('Death on the Nile', 1937, self.a2)
        self.l1.new_book('Five little pigs', 1942, self.a2)

    def print_author_test(self):
        self.assertEqual(self.a1, 'Shakespeare')
        self.assertEqual(self.a2, 'Agatha Christie')

    def print_book_test(self):
        self.assertEqual(self.b1, 'Hamlet (1601) by Shakespeare')
        self.assertEqual(self.b3, 'Death on the Nile (1942) by Agatha Christie')

    def check_author_book_lists(self):
        self.assertListEqual(self.a1.books, [self.b1, self.b2])

    def check_library_books_list(self):
        self.assertListEqual(self.l1.books, [self.b1, self.b2, self.b3, self.b4])

    def check_library_authors_list(self):
        self.assertListEqual(self.l1.authors, [self.a1, self.a2])

    def group_by_author_test(self):
        self.assertListEqual(self.l1.group_by_author(self.a1), [self.b1, self.b2])

    def group_by_year_test(self):
        self.assertListEqual(self.l1.group_by_year(1937), [self.b3])


# Big problem: It returns OK everytime, doesn't matter what wrong or good parameters I introduce
if __name__ == "__main__":
    unittest.main()
