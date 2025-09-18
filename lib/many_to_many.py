
class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self._name = value

    def contracts(self):
        return [contract for contract in Contract.all if contract.author==self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author==self ]
    
    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)

    def total_royalties(self):
        sum_royalties=0
        for contract in Contract.all:
            if contract.author==self:
                sum_royalties+=contract.royalties
        return sum_royalties
class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        self._title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("title must be a string")
        self._title = value

    def contracts(self):
        return [contract for contract in Contract.all if contract.book==self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book==self ]

class Contract:
    all=[]
    def __init__(self, author, book, date, royalties):
        self.author = author        # passe par le setter
        self.book = book            # passe par le setter
        self.date = date            # passe par le setter
        self.royalties = royalties  # passe par le setter
        Contract.all.append(self)

    # author
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an instance of Author")
        self._author = value

    # book
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise TypeError("book must be an instance of Book")
        self._book = value

    # date (chaîne simple pour coller au test)
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("date must be a string")
        self._date = value

    # royalties
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise TypeError("royalties must be an integer")
        self._royalties = value
        
    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in cls.all if contract.date==date]
