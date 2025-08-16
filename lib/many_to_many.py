# lib/many_to_many.py

class Book:
    def __init__(self, title):
        self.title = title


class Author:
    def __init__(self, name):
        self.name = name


class Contract:
    def __init__(self, book, author, date):
        self.book = book
        self.author = author
        self.date = date
class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        return [c.author for c in self.contracts()]


class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [c for c in Contract.all if c.author == self]

    def books(self):
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


class Contract:
    all = []  # keep track of all contracts

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an Author")
        if not isinstance(book, Book):
            raise TypeError("book must be a Book")
        if not isinstance(date, str):
            raise TypeError("date must be a str")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # validate author
        if not isinstance(author, Author):
            raise Exception("author must be an Author")

        # validate book
        if not isinstance(book, Book):
            raise Exception("book must be a Book")

        # validate date
        if not isinstance(date, str):
            raise Exception("date must be a string")

        # validate royalties
        if not isinstance(royalties, int):
            raise Exception("royalties must be an int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]

