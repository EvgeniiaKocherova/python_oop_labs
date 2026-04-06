def validate_title(title):
    if not title or not isinstance(title, str):
        raise ValueError("Название должно быть непустой строкой")

def validate_author(author):
    if not author or not isinstance(author, str):
        raise ValueError("Автор должен быть непустой строкой")
    
def validate_year(year):
    if not isinstance(year, int) or year < 1450 or year > 2026:
        raise ValueError("Год должен быть числом от 1450 до 2026")
    
def validate_pages(pages):
    if pages is None:
        raise ValueError("Количество страниц должно быть указано")
    if not isinstance(pages, int) or pages <= 0:
        raise ValueError("Количество страниц должно быть положительным числом")