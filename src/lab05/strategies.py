# ============= стратегии сортировки =============

def by_title(item):
    """Сортировка по названию"""
    return item.title.lower()


def by_year(item):
    """Сортировка по году издания"""
    return item.year


def by_pages(item):
    """Сортировка по количеству страниц"""
    return item.pages


# ============= функции-фильтры) =============

def is_available(item):
    """Фильтр: только доступные книги (в наличии)"""
    return item._is_available


def is_downloaded(item):
    """Фильтр: только скачанные книги (для AudioBook и EBook)"""
    return hasattr(item, '_is_downloaded') and item._is_downloaded


# ============= фабрики функций =============

def make_year_filter(min_year):
    """Фабрика: создаёт фильтр по минимальному году"""
    def filter_fn(item):
        return item.year >= min_year
    return filter_fn


def make_pages_filter(min_pages, max_pages):
    """Фабрика: создаёт фильтр по диапазону страниц"""
    def filter_fn(item):
        return min_pages <= item.pages <= max_pages
    return filter_fn


# ============= функции map()  =============

def to_short_string(item):
    """Преобразование объекта в короткую строку"""
    return f"{item.title} ({item.year})"


def extract_title_author(item):
    """Извлечение названия и автора в виде словаря"""
    return {
        'title': item.title,
        'author': item.author,
        'year': item.year
    }