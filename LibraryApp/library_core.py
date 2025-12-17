from models import Book
from storage import Storage_libr

class Library:
    """Class for Storage of Libary"""
    def __init__(self, storage : Storage_libr):
        self.file = storage.filename
        self.libr = storage.load()

    def __str__(self):
        lib = str(self.file)
        lib = lib.split('.')
        return lib[0]
    
    def find(self, book: Book):
        with open(file=self.file, mode='r') as file:
            lines = file.readlines()

            if lines != "":
                for line in lines:
                    parts = line.split('|')
                    shablon_for_search = f"||{parts[2]}|{parts[3]}|{parts[4]}|"

                    if shablon_for_search == book.info:
                        return book.info
            else:
                print("File is empty")
                        
    def _find_add(self, book : Book): 
        with open(file=self.file, mode='r+') as file:
            same = 0
            lines = file.readlines()
            file.seek(0)
            file.truncate()

            if lines != "":
                for line in lines:
                    parts = line.split('|')
                    shablon_for_search = f"||{parts[2]}|{parts[3]}|{parts[4]}|"

                    if shablon_for_search == book.info:
                        count = int(parts[5])
                        book.count += count
                        line = book.info + f"{book.count}||\n"   
                        same = 1             
                    file.write(line)
                
                if same == 1:
                    return False
    
    def add_book(self, book: Book):
        res = self._find_add(book)
        if res != False:
            self.libr += book.info + f"{book.count}||\n"
            Storage_libr.save(self)

    def del_book(self, book : Book, del_count):
        with open(file=self.file, mode='r+') as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()

            if lines != "":
                for line in lines:
                    parts = line.split('|')
                    shablon_for_search = f"||{parts[2]}|{parts[3]}|{parts[4]}|"

                    if shablon_for_search == book.info:
                        count = int(parts[5])
                        if del_count > count:
                            del_count = count
                        book.count = count - del_count
                        line = book.info + f"{book.count}||\n"            
                    file.write(line)
                return del_count