# LibraryApp

**Первый проект по ООП на Python**

LibraryApp — простая система управления библиотекой с использованием принципов ООП и абстракций.

## Функционал

- Добавление книг в библиотеку
- Поиск книг:
  - по названию
  - по жанру
  - по типу (книга, eBook, аудиокнига)
- Аренда/покупка книг пользователями
- Разные типы пользователей:
  - Admin — добавление книг, управление библиотекой
  - Reader — просмотр и аренда книг
- Сохранение данных в файлы (`.txt`)

## Структура проекта

- `app.py` — основной файл для запуска и тестирования
- `storage.py` — классы для работы с файлами (Storage_libr, Storage_users)
- `models.py` — Book, User, Admin, Reader, Types
- `library_core.py` — класс Library и логика добавления/удаления книг
- `search.py` — стратегия поиска книг (Strategy Pattern)
- `library_2.txt` — пример данных книг
- `list_admins.txt` — пример списка админов
- `list_users.txt` — пример списка пользователей

## Используемые технологии

- Python 3.10+
- OOP (классы, наследование, абстрактные классы)
- Enum, статические и класс методы
- Работа с файлами
- Паттерн Strategy для поиска

## Пример использования

```python
from storage import Storage_libr, Storage_users
from models import Book, Reader, Types
from library_core import Library
from search import TitleSearch

# Создание хранилища
storage_books = Storage_libr("library_2.txt")
library = Library(storage_books)

# Создание пользователя
storage_users = Storage_users()
user = Reader("John Patrik", storage_users)

# Покупка книги
result = user.buy("harry potter 1", 2, library)
print(result)

# Поиск книги
line = TitleSearch.search("harry potter 1", library)
print(line)
