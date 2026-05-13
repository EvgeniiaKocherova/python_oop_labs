from lab01.model import Book
from lab03.models import AudioBook, EBook
from lab06.container import TypedCollection
from typing import List 

print("--------------" )
print("ЛР-6 — Generics и typing")
print("--------------" )

book1 = Book("Вишневый сад", "Чехов", 1904, 90)
book2 = Book("Война и мир", "Толстой", 1869, 1300)
audio1 = AudioBook("Мастер и Маргарита", "Булгаков", 1967, 480, 120, "Михайлов")
ebook1 = EBook("Собачье сердце", "Булгаков", 1925, 160, 2.5, "heart.fb2")


print("1. Создание типизированной коллекции TypedCollection[Book]")
print("---------------")

collection: TypedCollection[Book] = TypedCollection()

print("Добавляем объекты:")
collection.add(book1)
collection.add(book2)
collection.add(audio1)   
collection.add(ebook1)  

print(f"В коллекции {len(collection)} элемента:")
for i, item in enumerate(collection.get_all(), 1):
    print(f"  {i}. {item.title} — {type(item).__name__}")

print("--------------" )
print("2. Метод find()")
print("--------------" )

found = collection.find(lambda b: b.title == "Война и мир")
if found:
    print(f"Найдено: {found.title}, {found.year} г.")

not_found = collection.find(lambda b: b.title == "Несуществующая книга")
print(f"Поиск несуществующей: {not_found}")

print("--------------" )
print("3. Метод filter()")
print("--------------" )

old_books = collection.filter(lambda b: b.year < 1900)
print("Книги до 1900 года:")
for b in old_books:
    print(f"  {b.title} — {b.year} г.")

long_books = collection.filter(lambda b: b.pages > 300)
print("Книги длиннее 300 страниц:")
for b in long_books:
    print(f"  {b.title} — {b.pages} стр.")

print("--------------" )
print("4. Метод map() — тип результата меняется")
print("--------------" )

titles: List[str] = collection.map(lambda b: b.title)
print("map(lambda b: b.title) -> list[str]:")
for title in titles:
    print(f"  {title}")

years: List[int] = collection.map(lambda b: b.year)
print("\nmap(lambda b: b.year) -> list[int]:")
for year in years:
    print(f"  {year}")

descriptions: List[str] = collection.map(lambda b: f"'{b.title}' ({b.year})")
print("map() - короткие описания:")
for desc in descriptions:
    print(f"  {desc}")


print("--------------" )
print("5. Комбинация методов (filter + map)")
print("--------------" )

result = collection.filter(lambda b: b.year >= 1900)
result = [b.title for b in result]  
print("Названия книг после 1900 года:")
for title in result:
    print(f"  {title}")