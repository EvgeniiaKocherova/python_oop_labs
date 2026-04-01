# from validate import BookValidator

class Book:
    _catalog_of_books = []

    def __init__(self, title, author, year, pages, is_available=True):

        self._title = title
        self._author = author
        self._year = year
        self._pages = pages
        self._is_available = is_available

        if not title or not isinstance(title, str):
            raise ValueError("Название должно быть непустой строкой")
        if not author or not isinstance(author, str):
            raise ValueError("Автор должен быть непустой строкой")
        if not isinstance(year, int) or year < 1450 or year > 2026:
            raise ValueError("Год должен быть числом от 1450 до 2026")
        if pages is None:
            raise ValueError("Количество страниц должно быть указано")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")

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
        self._year = new_year
        
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