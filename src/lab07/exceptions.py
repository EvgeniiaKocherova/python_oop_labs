class ItemNotFoundError(Exception):
    """Книги нет в коллекции"""
    pass

class DuplicateItemError(Exception):
    """Книга с таким названием и автором уже существует"""
    pass