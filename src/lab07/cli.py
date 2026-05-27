from typing import List, Optional
from lab07.app import LibraryApp
from lab07.exceptions import ItemNotFoundError, DuplicateItemError
from lab07.storage import save, load


class CLI:
    def __init__(self, app: LibraryApp) -> None:
        self.app = app

    def _print_header(self, title: str) -> None:
        print("\n" + "=" * 60)
        print(f"  {title}")
        print("=" * 60)

    def _print_books(self, books: List[Book], title: str = "Список книг") -> None:
        if not books:
            print("Коллекция пуста")
            return
        self._print_header(title)
        print(f"{'№':<4} {'Название':<30} {'Автор':<20} {'Год':<6} {'Статус':<12}")
        print("-" * 80)
        for i, book in enumerate(books, 1):
            status = "в наличии" if book.is_available else "выдана"
            print(f"{i:<4} {book.title[:27]:<30} {book.author[:17]:<20} {book.year:<6} {status:<12}")
        print(f"\nВсего: {len(books)}")

    def _input(self, prompt: str, type_func=str, min_val=None, max_val=None):
        while True:
            try:
                val = type_func(input(prompt))
                if min_val is not None and val < min_val:
                    print(f"Минимум {min_val}")
                    continue
                if max_val is not None and val > max_val:
                    print(f"Максимум {max_val}")
                    continue
                return val
            except ValueError:
                print(f"Ошибка: введите {type_func.__name__}")

    def _create_book(self) -> Optional[Book]:
        self._print_header("Добавление книги")
        t = self._input("Тип (1-бумажная, 2-аудио, 3-электронная): ", int, 1, 3)
        title = self._input("Название: ")
        author = self._input("Автор: ")
        year = self._input("Год: ", int, 1450, 2026)
        pages = self._input("Страниц: ", int, 1)
        
    def _get_book_data(self) -> Optional[dict]:
        """Собирает данные о книге от пользователя (НЕ создаёт объект!)."""
        self._print_header("Добавление книги")
        
        data = {
            'type': self._input("Тип (1-бумажная, 2-аудио, 3-электронная): ", int, 1, 3),
            'title': self._input("Название: "),
            'author': self._input("Автор: "),
            'year': self._input("Год: ", int, 1450, 2026),
            'pages': self._input("Страниц: ", int, 1)
        }
        
        if data['type'] == 2:
            data['time'] = self._input("Длительность (мин): ", float, 0.1)
            data['reader'] = self._input("Чтец: ")
        elif data['type'] == 3:
            data['size'] = self._input("Размер (МБ): ", float, 0.01)
            data['file'] = self._input("Имя файла: ")
        
        return data

    def run(self) -> None:
        while True:
            print("\n" * 2)
            self._print_header("ГЛАВНОЕ МЕНЮ")
            print("""
1. Показать все книги
2. Добавить книгу
3. Удалить книгу
4. Найти по названию
5. Найти по автору
6. Показать доступные
7. Фильтр по годам
8. Выдать книгу
9. Вернуть книгу
10. Сортировка
11. Статистика
12. Очистить коллекцию
13. Сохранить
14. Загрузить из файла
0. Выход""")
            choice = self._input("Выберите: ", int, 0, 14)

            try:
                if choice == 0:
                    save(self.app.get_all_books())
                    print("Данные сохранены. До свидания!")
                    break
                elif choice == 1:
                    self._print_books(self.app.get_all_books())
                elif choice == 2:
                    book = self._create_book()
                    if book:
                        self.app.add_book(book)
                elif choice == 3:
                    title = self._input("Название книги для удаления: ")
                    confirm = input(f"Удалить '{title}'? (y/n): ").lower()
                    if confirm == 'y':
                        self.app.remove_book(title)
                        print("Удалено")
                elif choice == 4:
                    title = self._input("Название: ")
                    book = self.app.find_book_by_title(title)
                    if book:
                        print(f"\n{book}")
                    else:
                        print("Не найдено")
                elif choice == 5:
                    author = self._input("Автор: ")
                    books = self.app.find_books_by_author(author)
                    self._print_books(books, f"Книги {author}")
                elif choice == 6:
                    self._print_books(self.app.get_available_books(), "Доступные книги")
                elif choice == 7:
                    min_y = self._input("Год от: ", int, 1450, 2026)
                    max_y = self._input("Год до: ", int, min_y, 2026)
                    books = self.app.filter_books(lambda b: min_y <= b.year <= max_y)
                    self._print_books(books, f"Книги {min_y}-{max_y} гг.")
                elif choice == 8:
                    self.app.give_book(self._input("Название: "))
                    print("Книга выдана")
                elif choice == 9:
                    self.app.return_book(self._input("Название: "))
                    print("Книга возвращена")
                elif choice == 10:
                    print("1. По названию\n2. По году\n3. По страницам\n4. По автору")
                    opt = self._input("Выберите: ", int, 1, 4)
                    keys = [lambda b: b.title.lower(), lambda b: b.year, lambda b: b.pages, lambda b: b.author.lower()]
                    self.app.sort_books(keys[opt - 1])
                    print("Отсортировано")
                elif choice == 11:
                    stats = self.app.get_statistics()
                    print(f"\nВсего: {stats['total']}\nДоступно: {stats['available']}\nВыдано: {stats['checked_out']}")
                elif choice == 12:
                    if self._input("Очистить всё? (y/n): ") == 'y':
                        self.app.clear_collection()
                elif choice == 13:
                    save(self.app.get_all_books())
                    print("Сохранено")
                elif choice == 14:
                    if self._input("Загрузить? (y/n): ") == 'y':
                        self.app.clear_collection()
                        for b in load():
                            try:
                                self.app.add_book(b)
                            except DuplicateItemError:
                                pass
                        print("Загружено")
            except (ItemNotFoundError, DuplicateItemError) as e:
                print(f"\nОшибка: {e}")
            except Exception as e:
                print(f"\nНепредвиденная ошибка: {e}")

            input("\nНажмите Enter...")