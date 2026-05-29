from typing import List, Optional, Dict, Any, Callable
from lab01.model import Book
from lab03.models import AudioBook, EBook
from lab05.collection import StrategyCollection
from exceptions import DuplicateItemError, ItemNotFoundError


class LibraryApp:
    def __init__(self) -> None:
        self._collection = StrategyCollection()

    def get_all_books(self) -> List[Book]:
        '''Вывод всех книг'''
        return self._collection.get_all()
    
    def create_book_from_data(self, data: dict) -> Book:
        """Создаёт книгу из словаря с данными (фабричный метод)."""
        book_type = data['type']
        
        if book_type == 1:
            return Book(
                title=data['title'],
                author=data['author'],
                year=data['year'],
                pages=data['pages']
            )
        elif book_type == 2:
            return AudioBook(
                title=data['title'],
                author=data['author'],
                year=data['year'],
                pages=data['pages'],
                time=data['time'],
                reader=data['reader']
            )
        elif book_type == 3:
            return EBook(
                title=data['title'],
                author=data['author'],
                year=data['year'],
                pages=data['pages'],
                size=data['size'],
                file=data['file']
            )
        else:
            raise ValueError(f"Неизвестный тип книги: {book_type}")

    def add_book(self, book: Book) -> None:
        '''Добавить книгу'''
        if any(book == existing for existing in self._collection.get_all()):
            raise DuplicateItemError(f"Книга '{book.title}' автора '{book.author}' уже существует")
        self._collection.add(book)

    def add_book_from_data(self, data: dict) -> None:
        '''Добавить книгу из словаря с данными'''
        book = self.create_book_from_data(data)
        self.add_book(book)

    def remove_book(self, title: str) -> bool:
        '''Убрать книгу'''
        book = self.find_book_by_title(title)
        if not book:
            raise ItemNotFoundError(f"Книга '{title}' не найдена")
        self._collection.remove(book)
        return True
    
    def find_books_by_author(self, author: str) -> List[Book]:
        """Найти все книги автора."""
        return [book for book in self._collection.get_all() 
                if book.author.lower() == author.lower()]

    def find_book_by_title(self, title: str) -> Optional[Book]:
        """Найти книгу по названию."""
        for book in self._collection.get_all():
            if book.title.lower() == title.lower():
                return book
        return None

    def filter_books(self, predicate: Callable[[Book], bool]) -> List[Book]:
        '''Отфильтровать книги'''
        return [b for b in self._collection.get_all() if predicate(b)]

    def sort_books(self, key_func: Callable[[Book], Any]) -> None:
        '''Отсортировать книги по ключу'''
        self._collection.sort_by(key_func)

    def get_available_books(self) -> List[Book]:
        '''Вывести книги в наличии'''
        return self.filter_books(lambda b: b.is_available)

    def give_book(self, title: str) -> None:
        '''Выдать книгу'''
        book = self.find_book_by_title(title)
        if not book:
            raise ItemNotFoundError(f"Книга '{title}' не найдена")
        book.give_book()

    def return_book(self, title: str) -> None:
        '''Вернуть книгу'''
        book = self.find_book_by_title(title)
        if not book:
            raise ItemNotFoundError(f"Книга '{title}' не найдена")
        book.return_book()

    def get_statistics(self) -> Dict[str, Any]:
        '''Получить статистику библиотеки'''
        books = self._collection.get_all()
        available = sum(1 for b in books if b.is_available)
        return {
            "total": len(books),
            "available": available,
            "checked_out": len(books) - available,
            "audio_books": sum(1 for b in books if isinstance(b, AudioBook)),
            "ebooks": sum(1 for b in books if isinstance(b, EBook)),
            "physical_books": sum(1 for b in books if isinstance(b, Book) and not isinstance(b, (AudioBook, EBook)))}

    def clear_collection(self) -> None:
        '''Очистить коллекцию'''
        self._collection = StrategyCollection()

    def count(self) -> int:
        '''Вывести количество книг'''
        return len(self._collection.get_all())