from typing import List, Callable, Any
from lab01.model import Book


class StrategyCollection:
    """Коллекция с поддержкой стратегий сортировки, фильтрации и map"""

    def __init__(self):
        self._items = []

    def __str__(self):
        return f"StrategyCollection, {len(self)} объектов"

    def add(self, item):
        """Добавление объекта в коллекцию"""
        if not isinstance(item, Book):
            raise ValueError("Можно добавлять только объекты Book или его наследников")
        self._items.append(item)

    def remove(self, item):
        """Удаление объекта из коллекции"""
        if not isinstance(item, Book):
            raise ValueError("Можно удалять только объекты Book")
        self._items.remove(item)

    def get_all(self):
        """Показать список книг"""
        return self._items

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    # ============= новые методы =============

    def sort_by(self, key_func):
        """Сортировка коллекции по переданной функции-ключу."""
        self._items.sort(key=key_func)
        return self

    def filter_by(self, func):
        """Фильтрация коллекции по переданной функции"""
        self._items = list(filter(func, self._items))
        return self

    def apply(self, func):
        """Применить функцию ко всем элементам коллекции."""
        self._items = list(map(func, self._items))
        return self

    def transform(self, func):
        """Преобразовать коллекцию с помощью map (возвращает новый список)."""
        return list(map(func, self._items))