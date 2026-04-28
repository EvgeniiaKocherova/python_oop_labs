from abc import ABC
from lab01.model import Book as BaseBook
from lab03.models import AudioBook as BaseAudioBook, EBook as BaseEBook
from lab04.interfaces import Printable, Comparable, Downloadable


class Book(BaseBook, Printable, Comparable):
    def to_string(self):
        """Возвращает детальную информацию о книге"""
        return f"Книга: '{self._title}' | Автор: {self._author} | {self._year} г. | {self._pages} стр."
    
    def compare_to(self, other):
        """Сравнение по году издания"""
        try:
            other_year = other._year if hasattr(other, '_year') else other.year
        except AttributeError:
            raise TypeError(f"Невозможно сравнить Book с типом {type(other)}")
        
        if self._year < other._year:
            return -1
        elif self._year > other._year:
            return 1
        return 0
    
    def __str__(self):
        """Красивый вывод"""
        if self._is_available:
            status = "в наличии"
        else:
            status = "не в наличии"
        return f'{self._title} | {self._author} | {self._year} | {status}'


class AudioBook(BaseAudioBook, Printable, Comparable, Downloadable):
    def to_string(self) -> str:
        """Реализация Printable"""
        if self._is_downloaded:
            status = "скачана" 
        else:
            "не скачана"
        return f"Аудиокнига: '{self._title}' | {self._author} | Длительность: {self._time} мин. | Чтец: {self._reader}"
    
    def compare_to(self, other):
        """Сравнение по длительности"""
        if not isinstance(other, AudioBook):
            raise TypeError("Можно сравнивать только с объектами AudioBook")
        if self._time < other._time:
            return -1
        elif self._time > other._time:
            return 1
        return 0
    
    def is_downloaded(self):
        """Реализация Downloadable"""
        return self._is_downloaded
    

class EBook(BaseEBook, Printable, Comparable, Downloadable):
    def to_string(self) -> str:
        """Реализация Printable"""
        status = "скачана" if self._is_downloaded else "не скачана"
        return f"Электронная книга: '{self._title}' | {self._author} | Формат: {self._file} | Размер: {self._size} МБ"
    
    def compare_to(self, other) -> int:
        """Сравнение по размеру файла"""
        if not isinstance(other, EBook):
            raise TypeError("Можно сравнивать только с объектами EBook")
        if self._size < other._size:
            return -1
        elif self._size > other._size:
            return 1
        return 0
    
    def is_downloaded(self) -> bool:
        """Реализация Downloadable"""
        return self._is_downloaded