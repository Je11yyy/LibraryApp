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

- Python 3.10
- OOP (классы, наследование, абстрактные классы)
- Enum, статические и класс методы
- Работа с файлами
- Паттерн Strategy для поиска

## Пример использования

```python
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

