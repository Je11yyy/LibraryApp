from abc import ABC, abstractclassmethod
from enum import Enum
from storage import Storage_libr, Admin_Storage, Reader_Storage


class Types(Enum):
    Book = 1
    EBook = 2
    AudioBook = 3

class Book:
    """Class for Book"""
    def __init__(self, name, genre, typeof: Types, count):
        self.info = {
            "name": name,
            "genre": genre,
            "type": typeof,
            "count": count
        }

class User(ABC):
    def __init__(self, name):
        self.name = name         

class Admin(User):
    def __init__(self, name, library):
        super().__init__(name)
        self.library = library
    
    def return_library_items(self):
        self.library.print_items()
           
class Reader(User):
    def __init__(self, name, data):
        super().__init__(name)
        self.inventory = data
    
    def get_inventory(self):
        return self.inventory

    def buy(self, name_of_book, count, library):
        from search import TitleSearch
        
        book_ = TitleSearch.search(name_of_book, library)
        book_buy = Book(book_['name'], book_['genre'], book_['type'], book_['count'])

        if book_buy == None:
            return False
        if book_buy.info["count"] == 0:
            return False
        count = library.del_book(book_buy, count)
        book_buy.info["count"] = count

        self.inventory.append(book_buy.info)
        return True
