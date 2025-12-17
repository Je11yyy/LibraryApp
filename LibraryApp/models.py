from abc import ABC
from enum import Enum
from storage import Storage_users


class Types(Enum):
    Book = 1
    EBook = 2
    AudioBook = 3

class Book:
    """Class for Book"""
    def __init__(self, name, genre, type: Types, count):
        self.info = f"||{name.center(18)}|{genre.center(10)}|{type.center(13)}|"
        self.count = count

    @classmethod
    def _from_str_(cls, s):
        parts = s.split('|')
        name = parts[2]
        genre = parts[3]
        type = parts[4]
        count = int(parts[5])
        return cls(name, genre, type, count)
    

class User(ABC):
    def __init__(self, name):
        self.name = name         

class Admin(User):
    def __init__(self, name, library):
        super().__init__(name)
        self.library = str(library)
        Storage_users.save(self)
        
class Reader(User):
    def __init__(self, name, storage:Storage_users):
        super().__init__(name)
        self.inventory = storage.load()
    
    def get_inventory(self):
        return self.inventory

    def buy(self, name_of_book, count, library):
        from search import TitleSearch
        
        str = TitleSearch.search(name_of_book, library)
        book_buy = Book._from_str_(str)
        if book_buy.count == 0:
            return "Book isnt in Storage of Library"
        count = library.del_book(book_buy, count)
        self.inventory.append(f"{book_buy.info}{count}||")
        Storage_users.save(self)
        return "You Bought succesfuly"