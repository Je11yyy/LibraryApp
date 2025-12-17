from storage import Storage_libr, Storage_users
from models import Book, Reader, Types
from library_core import Library

def main():
    # Создание хранилища книг
    storage_books = Storage_libr('library_2.txt')
    library = Library(storage_books)

    # Создание хранилища пользователей
    storage_users = Storage_users()

    # Создание пользователя
    user = Reader('Jhon Patrik', storage_users)

    # Пример покупки книги
    result = user.buy('harry potter 1', 2, library)
    print(result)

if __name__ == "__main__":
    main()
