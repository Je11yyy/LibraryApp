from storage import Storage_libr, Load_reader
from models import Types, Book, Admin, Reader
from library_core import Library

def main():
    # Создание хранилища книг
    storage_books = Storage_libr('library.txt')
    library = Library(storage_books)

    book = Book('harry potter 1','fantasy', 'Book', 1)
    library.add_book(book)
    # Создание хранилища пользователей
    storage_users = Load_reader()

    # Создание пользователя
    user = Reader('Jhon Patrik', storage_users)

    # Пример покупки книги
    result = user.buy('harry potter 1', 2, library, storage_books)
    print(result)



if __name__ == "__main__":
    main()
