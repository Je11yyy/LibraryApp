# LibraryApp

**Первый проект по ООП на Python**

LibraryApp — простая система управления библиотекой с использованием принципов ООП и абстракций.

## Функционал

- Добавление книг в библиотеку
- Поиск книг:
  - по названию
  - по жанру
  - по типу (книга, eBook, аудиокнига)
- Покупка книг пользователями
- Разные типы пользователей:
  - Admin — управление библиотекой
  - Reader — просмотр и покупка книг
- Сохранение данных в файлы (`.json`)

## Структура проекта

- `app.py` — основной файл для запуска и тестирования
- `storage.py` — классы для работы с файлами (Storage_libr, Storage_users)
- `models.py` — Book, User, Admin, Reader, Types
- `library_core.py` — класс Library и логика добавления/удаления книг
- `search.py` — стратегия поиска книг (Strategy Pattern)
- `library.json` — пример данных книг
- `admins.json` — пример списка админов
- `readers.json` — пример списка пользователей

## Используемые технологии

- Python 3.10
- OOP (классы, наследование, абстрактные классы)
- Enum, статические и класс методы
- Работа с файлами
- Паттерн Strategy для поиска

## Пример использования

```python
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
    reader_storage.save(user)
    if result == True:
        print("You bought succsesfuly")
    else:
        print("Error no such book in library now")



if __name__ == "__main__":
    main()
