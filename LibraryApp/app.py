from storage import Storage_libr, Reader_Storage, Admin_Storage
from models import Types, Book, Admin, Reader
from library_core import Library

def main():
    # Создание хранилища книг
    storage_libr = Storage_libr('library.json')
    data_library = storage_libr.load()
    library = Library(storage_libr, data_library)

    # Создаем книгу
    book = Book('harry potter 1','fantasy', 'Book', 2)
    book2 = Book('harry potter 2','fantasy', 'Book', 2)

    # Добавляем в библиотеку и сохраняем в файл
    library.add_book(book)
    storage_libr.save(library)

    library.add_book(book2)
    storage_libr.save(library)
    # Создание хранилища пользователей
    reader_storage = Reader_Storage()
    name = 'Jhon Patrik'
    data_users = reader_storage.load(name)
    # Создание пользователя
    user = Reader(name, data_users)

    # Пример покупки книги
    result = user.buy('harry potter 1', 1, library)
    result = user.buy('harry potter 2', 2, library)

    reader_storage.save(user)
    if result == True:
        print("You bought succsesfuly")
    else:
        print("Error no such book in library now")



if __name__ == "__main__":
    main()
