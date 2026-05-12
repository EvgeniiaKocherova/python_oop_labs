from typing import TypeVar, Generic, Callable, Optional, List

T = TypeVar('T')
R = TypeVar('R')


class TypedCollection(Generic[T]):
    """Типизированная коллекция (Library из ЛР2)"""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def __str__(self) -> str:
        return f"TypedCollection, {len(self)} элементов"
    
    def add(self, item: T) -> None:
        """Добавление элемента в коллекцию"""
        self._items.append(item)
    
    def remove(self, item: T) -> None:
        """Удаление элемента из коллекции"""
        self._items.remove(item)
    
    def get_all(self) -> List[T]:
        """Возвращает копию списка элементов"""
        return self._items.copy()
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """Возвращает первый элемент, удовлетворяющий условию"""
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        """Возвращает список всех элементов, удовлетворяющих условию"""
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> List[R]:
        """Применяет функцию к каждому элементу, возвращает список результатов"""
        return [transform(item) for item in self._items]