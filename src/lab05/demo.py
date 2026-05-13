from lab01.model import Book
from lab03.models import AudioBook, EBook
from lab05.collection import StrategyCollection
from lab05.strategies import *

book1 = Book("Вишневый сад", "Антон Павлович Чехов", 1904, 89)
book2 = Book("Война и мир", "Лев Толстой", 1869, 1300)
audio1 = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 2.0, "Михайлов И. Е.")
ebook1 = EBook("Собачье сердце", "Булгаков М.А.", 1925, 160, 1.1, "heart.fb2")
audio2 = AudioBook("Отцы и дети", "Иван Тургенев", 1862, 300, 1.5, "Иванов А. И.")

collection = StrategyCollection()
for item in [book1, book2, audio1, ebook1, audio2]:
    collection.add(item)

print(f"Создана коллекция из {len(collection)} объектов")

print('----------------------------------------------')
print("1. Стратегии сортировки через sorted()")
print('----------------------------------------------')

print("Сортировка по названию:")
for item in sorted(collection.get_all(), key=by_title):
    print(f"{item.title}")

print(' ')
print("Сортировка по году:")
for item in sorted(collection.get_all(), key=by_year):
    print(f"{item.title} - {item.year} г.")

print(' ')
print("Сортировка по страницам:")
for item in sorted(collection.get_all(), key=by_pages):
    print(f"{item.title} - {item.pages} стр.")
print(' ')

print('----------------------------------------------')
print("2. Фильтрация через filter()")
print('----------------------------------------------')
print(' ')

print("Только книги в наличии:")
available_books = list(filter(is_available, collection.get_all()))
for item in available_books:
    status = "в наличии" 
    print(f"{item.title} — {status}")

print(' ')
print("Только скачанные книги:")
downloaded_books = list(filter(is_downloaded, collection.get_all()))
if downloaded_books:
    for item in downloaded_books:
        print(f"{item.title}")
else:
    print("нет скачанных книг")


print('----------------------------------------------')
print("3. Преобразование через map()")
print('----------------------------------------------')

print(' ')
print("Короткие строки (название + год):")
short_strings = list(map(to_short_string, collection.get_all()))
for s in short_strings:
    print(f"{s}")

print(' ')
print("Извлечение полей (словари):")
extracted = list(map(extract_title_author, collection.get_all()))
for d in extracted:
    print(f"{d}")

print('----------------------------------------------')
print("4. Фабрика функций")
print('----------------------------------------------')

print(' ')
filter_after_1900 = make_year_filter(1900)
filtered_by_year = list(filter(filter_after_1900, collection.get_all()))
print("Книги после 1900 года:")
for item in filtered_by_year:
    print(f"{item.title} - {item.year} г.")

print(' ')
filter_pages_200_500 = make_pages_filter(200, 500)
filtered_by_pages = list(filter(filter_pages_200_500, collection.get_all()))
print("Книги с количеством страниц от 200 до 500:")
for item in filtered_by_pages:
    print(f"{item.title} - {item.pages} стр.")

print('----------------------------------------------')
print("5. Методы коллекции sort_by() и filter_by()")
print('----------------------------------------------')

coll2 = StrategyCollection()
for item in [book1, book2, audio1, ebook1, audio2]:
    coll2.add(item)

print(' ')
print("до сортировки:")
for item in coll2.get_all():
    print(f"{item.title} - {item.year}")

print(' ')
coll2.sort_by(by_year)
print("после sort_by(by_year):")
for item in coll2.get_all():
    print(f"{item.title} - {item.year}")

coll3 = StrategyCollection()
for item in [book1, book2, audio1, ebook1, audio2]:
    coll3.add(item)

print(' ')
print("Фильтрация через filter_by(is_available):")
coll3.filter_by(is_available)
for item in coll3.get_all():
    print(f"{item.title}")

print('----------------------------------------------')
print("6. Сравнение lambda и именованной функции")
print('----------------------------------------------')

print(' ')
sorted_lambda = sorted(collection.get_all(), key=lambda x: x.year)
print("Через lambda (сортировка по году):")
for item in sorted_lambda[:3]:
    print(f"{item.title} - {item.year}")

print(' ')
sorted_named = sorted(collection.get_all(), key=by_year)
print("Через именованную функцию by_year():")
for item in sorted_named[:3]:
    print(f"{item.title} - {item.year}")