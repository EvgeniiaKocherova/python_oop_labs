from model import Book
class Library:
    def __init__(self):
        self._items = []

    def __str__(self):
        return f"Библиотека, {len(self)} книг"

    def add(self, book):
        if not isinstance(book, Book):
            raise ValueError("Можно добавлять только объекты Book")
        for old_book in self._items:
            if book == old_book:
                raise ValueError("Книга уже добавлена в коллекцию")
        self._items.append(book)

    def remove(self, book):
        if not isinstance(book, Book):
            raise ValueError("Можно удалять только объекты Book")
        self._items.remove(book)

    def get_all(self):
        return self._items
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def find_by_title(self, title):
        for book in self._items:
            if book.title == title:
                return book
        return None
    
    def find_by_author(self, author):
        list_of_books = []
        for book in self._items:
            if book.author == author:
                list_of_books.append(book)
        return list_of_books
