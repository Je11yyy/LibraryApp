from abc import ABC, abstractclassmethod
from enum import Enum
from storage import Storage_libr, Load_reader, Save_admin, Save_reader
import os

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
    def from_str(cls, s):
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
        self.library = library
        Save_admin.save(self)
    
    def return_library_items(self):
        self.library.print_items()
           
class Reader(User):
    def __init__(self, name, storage: Load_reader):
        super().__init__(name)
        self.inventory = storage.load()
    
    def get_inventory(self):
        return self.inventory

    def buy(self, name_of_book, count, library, storage: Storage_libr):
        from search import TitleSearch
        
        str = TitleSearch.search(name_of_book, library)
        if str == None:
            return "Book isnt in Storage of Library"
        book_buy = Book.from_str(str)
        if book_buy.count == 0:
            return "Book isnt in Storage of Library now"
        count = library.del_book(book_buy, count, storage)
        self.inventory.append(f"{book_buy.info}{count}||")
        # ЕСЛИ ЧИТАТЕЛЬ ЗАШЕЛ НА САЙТ К ПРИМЕРУ, 
        # ЗАРЕГ, НО НЕ КУПИЛ КНИГУ --> ТО ЕГО НЕТ СМЫСЛА ДЕРЖАТЬ В БАЗЕ
        Save_reader.save(self)
        return "You Bought succesfuly"
