class Book:
    def __init__(self, title: str):
        self.title = title

    def contracts(self):
        return [c for c in Contract.all if c.book is self]

    def authors(self):
        return [c.author for c in self.contracts()]


class Author:
    def __init__(self, name: str):
        self.name = name

    def contracts(self):
        return [c for c in Contract.all if c.author is self]

    def books(self):
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date: str, royalties: int):
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

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda c: c.date)
