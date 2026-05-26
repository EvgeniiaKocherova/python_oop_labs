class ItemNotFoundError(Exception):
    """Книги нет в коллекции"""
    pass

class DuplicateItemError(Exception):
    """Книга с таким названием и автором уже существует"""
    pass

class InvalidInputError(Exception):
    """Некорректный ввод"""
    pass

class ValidationError(Exception):
    """Ошибка валидации данных"""
    pass