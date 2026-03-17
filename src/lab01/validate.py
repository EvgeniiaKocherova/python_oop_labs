class BookValidator:
    """Класс для валидации данных книги"""
    
    @staticmethod
    def validate_title(title):
        """Проверка названия"""
        if not title or not isinstance(title, str):
            raise ValueError("Название должно быть непустой строкой")
        return title
    
    @staticmethod
    def validate_author(author):
        """Проверка автора"""
        if not author or not isinstance(author, str):
            raise ValueError("Автор должен быть непустой строкой")
        return author
    
    @staticmethod
    def validate_year(year):
        """Проверка года"""
        if not isinstance(year, int) or year < 1450 or year > 2026:
            raise ValueError("Год должен быть числом от 1450 до 2026")
        return year
    
    @staticmethod
    def validate_pages(pages):
        """Проверка страниц"""
        if pages is None:
            raise ValueError("Количество страниц должно быть указано")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        return pages