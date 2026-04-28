from abc import ABC, abstractmethod

class Printable(ABC):
    """Интерфейс для объектов, которые могут быть выведены в строковом представлении"""
    
    @abstractmethod
    def to_string(self):
        """Возвращает строковое представление объекта"""
        pass


class Comparable(ABC):
    """Интерфейс для сравниваемых объектов"""
    
    @abstractmethod
    def compare_to(self, other):
        """Сравнивает текущий объект с другим."""
        pass


class Downloadable(ABC):
    """Интерфейс для скачиваемых объектов"""
    
    @abstractmethod
    def download(self):
        """Скачивает объект"""
        pass
    
    @abstractmethod
    def is_downloaded(self):
        """Возвращает статус скачивания"""
        pass