from model import Book
from collection import Library

print("Сценарий 1. Базовые операции")
print("----------------------------------------------")
book1 = Book("Вишневый сад", "Антон Павлович Чехов", 1904, 89)
book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, False)
book3 = Book("Война и мир", "Лев Толстой", 1867, 1300)
book4 = Book("Отцы и дети", "Иван Тургенев", 1862, 300)

my_library = Library()
my_library.add(book1)
print("Добавили в библиотеку книги:")
my_library.add(book2)
my_library.add(book3)
my_library.add(book4)
print(my_library)
print("----------------------------------------------")
print("\nСодержимое библиотеки через get_all:")
print(my_library.get_all())

print("----------------------------------------------")
print("\nУдаляем книгу 'Мастер и Маргарита'")
my_library.remove(book2)
print("После удаления:")
for book in my_library:
    print(book)

print(f"\nТеперь в библиотеке {len(my_library)} книг")
print("----------------------------------------------")
print("\nПробуем добавить дубликат 'Вишневый сад':")
try:
    my_library.add(book1)
except ValueError as e:
    print(f"Ошибка: {e}")




print(" ")
print("----------------------------------------------")
print("----------------------------------------------")
print("Сценарий 2. Поиск книг")
print("----------------------------------------------")

print("\nИщем книгу 'Война и мир':")
found_book = my_library.find_by_title("Война и мир")
if found_book:
    print(f"Найдено: {found_book}")
else:
    print("Книга не найдена")

print("----------------------------------------------")

print("\nИщем книгу 'Преступление и наказание':")
found_book = my_library.find_by_title("Преступление и наказание")
if found_book:
    print(f"Найдено: {found_book}")
else:
    print("Книга не найдена")

print("----------------------------------------------")

print("\nИщем книги автора 'Лев Толстой':")
found_books = my_library.find_by_author("Лев Толстой")
if found_books:
    print(f"Найдено книг: {len(found_books)}")
    for book in found_books:
        print(f"  - {book}")
else:
    print("Книги не найдены")

print("----------------------------------------------")

print("\nИщем книги автора 'Фёдор Достоевский':")
found_books = my_library.find_by_author("Фёдор Достоевский")
if found_books:
    print(f"Найдено книг: {len(found_books)}")
    for book in found_books:
        print(f"  - {book}")
else:
    print("Книги не найдены")

print(" ")
print("----------------------------------------------")
print("----------------------------------------------")
print("Сценарий 3. итерация и магические методы")
print("----------------------------------------------")
print("\nСодержимое библиотеки через iter:")
for book in my_library:
    print(book)
print("----------------------------------------------")
print("использование len")
print(f"Длина списка книг в библиотеке: {len(my_library)}")
