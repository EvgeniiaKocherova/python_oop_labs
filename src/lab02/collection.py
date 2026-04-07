from model import Book
class Library:
    """Коллекция книг"""
    def __init__(self):
        self._items = []

    def __str__(self):
       """Красивый вывод библиотеки"""
       return f"Библиотека, {len(self)} книг"

    def add(self, book):
        """Добавление книги в коллекцию"""
        if not isinstance(book, Book):
            raise ValueError("Можно добавлять только объекты Book")
        for old_book in self._items:
            if book is old_book:
                raise ValueError("Книга уже добавлена в коллекцию")
        self._items.append(book)

    def remove(self, book):
        """Удаление книги из коллекции"""
        if not isinstance(book, Book):
            raise ValueError("Можно удалять только объекты Book")
        self._items.remove(book)

    def get_all(self):
        """Вывод содержимого библиотеки"""
        return self._items
    
    def __len__(self):
        """Количество книг в библиотеке"""
        return len(self._items)
    
    def __iter__(self):
        """Итерация по библиотеке"""
        return iter(self._items)
    
    def find_by_title(self, title):
        """Нахождение книги в библиотеке по названию"""
        for book in self._items:
            if book.title == title:
                return book
        return None
    
    def find_by_author(self, author):
        """Нахождение всех книг автора в библиотеке"""
        list_of_books = []
        for book in self._items:
            if book.author == author:
                list_of_books.append(book)
        return list_of_books
