from models import Book
from storage import Storage_libr
from search import TitleSearch
import json

class Library:
    """Class for Storage of Libary"""
    def __init__(self, storage: Storage_libr, data: list):
        self.file = storage.filename
        self.libr = data

    def __str__(self):
        lib = str(self.file)
        lib = lib.split('.')
        return lib[0]
                            
    def add_book(self, add_book: Book):
        try:
            with open(file=self.file, mode='r') as file:
                self.libr = json.load(file)
            found = False
            for book in self.libr:
                if book['name'] == add_book.info['name']:
                    found = True
                    book['count'] += add_book.info['count']
                    break
            
            if found == False:
                self.libr.append(add_book.info)
        except:
            self.libr.append(add_book.info)

    def del_book(self, book_buy : Book, buy_count):
        ## МОЖНО ТУТ ПРОПИСАТЬ TRY
        ## И ПЕРЕДЕЛАТЬ СОХРАНЕНИЕ
        try:
            with open(file=self.file, mode='r') as file:
                self.libr = json.load(file)
        
            if book_buy.info["count"] < buy_count:
                buy_count = book_buy.info["count"]
            rest_count = book_buy.info["count"] - buy_count

            for book in self.libr:
                if book == book_buy.info:
                    book['count'] = rest_count
                    break
        ###
            with open(file=self.file, mode='w') as file: 
                json.dump(self.libr, file, indent=4)
        except:
            buy_count = 0
        return buy_count
