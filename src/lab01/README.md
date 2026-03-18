# Лабараторная 1  

## Вариант: Библиотека / Книги  

### Описание проекта
Реализация класса `Book` для библиотечной системы. Класс моделирует книгу с основными характеристиками и методами работы.

### Сущности
- **Book** — книга (основной класс)
- (Остальные сущности из варианта: Author, LibraryCard, Publisher, Reader — могут быть добавлены в будущем)

### Реализованные возможности

#### Атрибуты экземпляра (закрытые поля)
- `_title` — название книги
- `_author` — автор
- `_year` — год издания
- `_pages` — количество страниц
- `_is_available` — доступность (True/False)

#### Атрибут класса
- `_catalog_of_books` — список всех созданных книг

#### Магические методы
- `__str__` — красивое представление книги для пользователя
- `__repr__` — техническое представление для разработчика
- `__eq__` — сравнение книг по названию и автору

#### Свойства (@property) и сеттеры
- Геттеры для всех атрибутов
- Сеттеры для `year` с валидацией данных
- Валидация учитывает состояние книги (нельзя менять данные, если книга выдана)

#### Бизнес-методы
- `give_book()` — выдача книги читателю
- `return_book()` — возврат книги в библиотеку
- `repair()` — отправка книги на реставрацию
- `show_catalog()` — метод класса для отображения всех книг

#### Валидация данных
Все проверки вынесены в отдельные методы:
- `_validate_title()`
- `_validate_author()`
- `_validate_year()`
- `_validate_pages()`

Код для реализации model.py:
```
from validate import BookValidator

class Book:
    _catalog_of_books = []

    def __init__(self, title, author, year, pages, is_available=True):
        self._title = BookValidator.validate_title(title)
        self._author = BookValidator.validate_author(author)
        self._year = BookValidator.validate_year(year)
        self._pages = BookValidator.validate_pages(pages)
        self._is_available = is_available

        Book._catalog_of_books.append(self)

    def __str__(self):
        if self._is_available: 
            status = "в наличии" 
        else: 
            status = "не в наличии"

        return f'{self._title} | {self._author} | {self._year} | {status}'
    
    def __repr__(self):
        return f"Book('{self._title}', '{self._author}', {self._year}, {self._pages}, {self._is_available})"
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self._title == other._title and self._author == other._author

    @property
    def title(self):
        """Геттер для названия"""
        return self._title
    
    @property
    def author(self):
        """Геттер для автора"""
        return self._author
    
    @property
    def year(self):
        """Геттер для года издания"""
        return self._year
    
    @property
    def pages(self):
        """Геттер для количества страниц"""
        return self._pages

    @year.setter
    def year(self, new_year):
        if not self._is_available:
            raise ValueError("Нельзя изменить год книги, которая выдана читателю")
        self._year = BookValidator.validate_year(new_year)
        
    def give_book(self):
        """Выдать книгу читателю"""
        if not self._is_available:
            print("Книги нет в наличии")
            return False
        self._is_available = False
        print("Книга выдана")
        return True
    
    def return_book(self):
        """Вернуть книгу в библиотеку"""
        if self._is_available:
            print("Книга в наличии в библиотеке")
            return False
        self._is_available = True
        print("Книга возвращена в библиотеку")
        return True
    
    def repair(self):
        """Отправить книгу на реставрацию (новый метод состояния)"""
        if not self._is_available:
            print("Нельзя отправить на реставрацию книгу, которая выдана")
            return False
        print(f"Книга '{self._title}' отправлена на реставрацию")
        return True
    
    @classmethod
    def show_catalog(cls):
        if not cls._catalog_of_books:
            print("Каталог книг пуст")
            return
        print("Каталог книг")
        cnt = 1
        for book in cls._catalog_of_books:
            print(f"{cnt}. {book}")
            cnt += 1
```
### Валидация реализована в отдельном файле validate.py
```
class BookValidator:
    """Класс для валидации данных книги"""
    
    @staticmethod
    def validate_title(title):
        """Проверка названия"""
        if not title or not isinstance(title, str):
            raise ValueError("Название должно быть непустой строкой")
        return title
    
    @staticmethod
    def validate_author(author):
        """Проверка автора"""
        if not author or not isinstance(author, str):
            raise ValueError("Автор должен быть непустой строкой")
        return author
    
    @staticmethod
    def validate_year(year):
        """Проверка года"""
        if not isinstance(year, int) or year < 1450 or year > 2026:
            raise ValueError("Год должен быть числом от 1450 до 2026")
        return year
    
    @staticmethod
    def validate_pages(pages):
        """Проверка страниц"""
        if pages is None:
            raise ValueError("Количество страниц должно быть указано")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        return pages
```

### Код для реализации demo.py:
```
from model import Book

print("===Создание книг===")
#Демонстрация создания книг
book1 = Book("Вишневый сад", "Антон Павлович Чехов", 1904, 89)
book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, False)
book3 = Book("Война и мир", "Лев Толстой", 1867, 1300)

print("Созданы следующие книги:")
print(book1)
print(book2)
print(book3)
print("            ")

print("===Разные выводы===")
#Демонстрация разных выводов
print("Обычный вывод (str):")
print(str(book1))
print("Технический вывод (repr):")
print(repr(book1))
print("            ")

print("===Сравнение книг===")
#Демонстрация сравнения книг
book4 = Book("Вишневый сад", "Антон Павлович Чехов", 1904, 89)
print("Сравниваем книги по названию и автору:")
print(f"book1 и book2 - разные книги: {book1 == book2}")
print(f"book1 и саму себя: {book1 == book1}")
print(f"book1 и book4 - одинаковые название и автор: {book1 == book4}")
print()
print("            ")

print("===Геттеры===")
#Демонстрация геттеров
print("Информация о первой книге:")
print(f"Название: {book1.title}")
print(f"Автор: {book1.author}")
print(f"Год издания: {book1.year}")
print(f"Количество страниц: {book1.pages}")
print("            ")

print("===Сеттеры===")
#Демонстрация сеттеров
print(f"Старый год book1: {book1.year}")
book1.year = 2024
print(f"Новый год book1: {book1.year}")

print(f"Книга после изменений: {book1}")
print("            ")

print("===Атрибут класса===")
#Демонстрация атрибутов класса
print("Список всех созданных книг:")
print(Book._catalog_of_books)
print("Список через экземпляр book1:")
print(book1._catalog_of_books)
print(f"Всего создано книг: {len(Book._catalog_of_books)}")
print("       ")

print("===Бизнес-методы===")
print(f"Книга до выдачи: {book2}")  

print("Пытаемся выдать book2...")
book2.give_book()  

print(f"Книга до выдачи: {book3}")  
print("Выдаем book3...")
book3.give_book()
print(f"Книга после выдачи: {book3}")

print("Возвращаем book3...")
book3.return_book()
print(f"Книга после возврата: {book3}")
print("            ")

print("===Метод класса show_catalog===")
Book.show_catalog()
print("            ")

print("===Обработка ошибок при создании===")
try:
    bad_book = Book("", "Автор", 2000, 100)
except ValueError as e:
    print(f"Ошибка при пустом названии: {e}")

try:
    bad_book = Book("Название", "Автор", 1400, 100)  
except ValueError as e:
    print(f"Ошибка при старом годе: {e}")

try:
    bad_book = Book("Название", "Автор", 2000, -50)  
except ValueError as e:
    print(f"Ошибка при страницах: {e}")
print("            ")

try:
    bad_book = Book("Название", "", 1600, 1000)
except ValueError as e:
    print(f"Ошибка при пустом авторе: {e}")

print("===Демонстрация поведения, зависящего от состояния===")
print(f"Книга до выдачи: {book3}")
print("Пытаемся изменить год выданной книги:")
try:
    book3.give_book()  
    print("Книга выдана, теперь пробуем изменить год:")
    book3.year = 2025  
except ValueError as e:
    print(f"Ошибка: {e}")

print("\n===Демонстрация метода реставрации===")
book1.repair()  
book3.repair()


```
## Пример запуска demo.py  
![скриншот выполения запуска demo.py](../../images/lab01/img01.png)  

![скриншот выполения запуска demo.py](../../images/lab01/img02.png)

