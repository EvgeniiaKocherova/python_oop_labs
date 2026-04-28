from lab04.models import Book, AudioBook, EBook, Printable, Comparable, Downloadable
from lab02.collection import Library


# ============= УНИВЕРСАЛЬНАЯ ФУНКЦИЯ, РАБОТАЮЩАЯ ЧЕРЕЗ ИНТЕРФЕЙС =============

def print_all(items: list[Printable]) -> None:
    """Функция, работающая с любыми Printable объектами."""
    print("\n--- Вывод через интерфейс Printable ---")
    for item in items:
        print(f"  {item.to_string()}")


print("=" * 60)

book1 = Book("Вишневый сад", "Антон Павлович Чехов", 1904, 89)
audio1 = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 2.0, "Михайлов И. Е.")
ebook1 = EBook("Война и мир", "Лев Толстой", 1867, 1300, 60.1, "warnpeace.epub")
audio2 = AudioBook("Отцы и дети", "Иван Тургенев", 1862, 300, 1.5, "Иванов А. И.")
audio3 = AudioBook("Евгений Онегин", "Пушкин А.С.", 1833, 224, 8.0, "Петров П.П.")
ebook2 = EBook("Собачье сердце", "Булгаков М.А.", 1925, 160, 1.1, "heart.fb2")

lib = Library()
for item in [book1, audio1, ebook1, audio2, audio3, ebook2]:
    lib.add(item)

print(f"В библиотеке {len(lib)} книг:")
for i, book in enumerate(lib, 1):
    print(f"{i}. {book}")

# 1. Интерфейс как тип
print_all(lib.get_all())
print(" ")
# 2. Проверка isinstance
print("--- Проверка через isinstance ---")
for book in [book1, audio1, ebook1]:
    print(f"\n{book.title}:")
    print(f"  Printable?   {isinstance(book, Printable)}")
    print(f"  Comparable?  {isinstance(book, Comparable)}")
    print(f"  Downloadable? {isinstance(book, Downloadable)}")

# 3. Сравнение через Comparable
print(" ")
print("--- Сравнение через Comparable ---")
result = book1.compare_to(ebook1)
if result < 0:
    print(f"'{book1.title}' ({book1.year}) старше, чем '{ebook1.title}' ({ebook1.year})")
else:
    print(f"'{ebook1.title}' ({ebook1.year}) старше, чем '{book1.title}' ({book1.year})")

# 4. Скачивание через Downloadable
print(" ")
print("--- Скачивание через Downloadable ---")
for book in lib.get_all():
    if isinstance(book, Downloadable):
        print(f"{book.title}: ")
        book.download()