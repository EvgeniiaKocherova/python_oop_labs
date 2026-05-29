import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from lab07.exceptions import DuplicateItemError
from lab07.app import LibraryApp
from lab07.cli import CLI
from lab07.storage import load


def main() -> None:
    """Главная функция приложения."""
    print("Добро пожаловать в библиотечную систему  ૮₍ ` ꒳ `₎ა ")
    
    app = LibraryApp()
    
    print("Загрузка данных...")
    saved_books = load()
    
    for book in saved_books:
        try:
            app.add_book(book)
        except DuplicateItemError:  
            print(f"Дубрикат: {book.title} пропущен")
    
    print(f"Загружено {len(saved_books)} книг\n")
    
    ui = CLI(app)
    
    try:
        ui.run()
    except KeyboardInterrupt:
        print("\n\nПринудительное завершение...")
        from lab07.storage import save
        save(app.get_all_books())
        print("Данные сохранены.")


if __name__ == "__main__":
    main()