from lab02.collection import Library
from lab01.model import Book
from lab03.models import AudioBook, EBook

print("Сценарий 1. Создание книг и вывод")
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
print("---------------------------------------------------")

print(" ")

print("---------------------------------------------------")
print("Сценарий 2. Полиморфизм")
print("----Скачивание книг----")
for book in lib.get_all():
    book.download()  

print("---------------------------------------------------")

print("Статус после скачивания")
for book in lib.get_all():
    if hasattr(book, '_is_downloaded'):
        status = "скачана" if book._is_downloaded else "не скачана"
        print(f"{book.title}: {status}")


print(" ")
print("---------------------------------------------------")
print("Сценарий 3. Демонстрация isinstance()")
print("---------------------------------------------------")

print("Все аудиокниги в библиотеке")
for book in lib.get_all():
    if isinstance(book, AudioBook):
        print(f"{book.title} — чтец: {book._reader}, время: {book._time} мин.")
print("---------------------------------------------------")
print("Все электронные книги в библиотеке")
for book in lib.get_all():
    if isinstance(book, EBook):
        print(f"{book.title} — формат: {book._file}, размер: {book._size} МБ")
print("---------------------------------------------------")
print("Фильтрация: только скачанные аудиокниги")
for book in lib.get_all():
    if isinstance(book, AudioBook) and book._is_downloaded:
        print(f"{book.title} готова к прослушиванию")
print(" ")
print("---------------------------------------------------")
print("Сценарий 4. Уникальные методы дочерних классов")
print("---------------------------------------------------")

print("Изменение скорости аудиокниги")
print(f"До: {audio1}")
audio1.change_speed(1.8)
print(f"После: {audio1}")

print("---------------------------------------------------")
print(f"До: {audio2}")
audio2.change_speed(0.8)
print(f"После: {audio2}")

print("---------------------------------------------------")
print("добавление цитат в электронную книгу")
print(f"До: {ebook1}")
ebook1.quote("«Рукописи не горят»")
ebook1.quote("«Никогда и ничего не просите!»")
ebook1.quote("«Трусость — самый страшный порок»")
print(f"После добавления 3 цитат: {ebook1}")
print("---------------------------------------------------")
print(f"До: {ebook2}")
ebook2.quote("«Успевает всюду тот, кто никуда не торопится»")
print(f"После добавления 1 цитаты: {ebook2}")

# # Демонстрация метода repair() из базового класса (работает и для наследников)
# print(" Метод базового класса для наследников")
# print(f"Отправляем '{audio3.title}' на реставрацию:")
# audio3.repair()
# print(f"Отправляем '{ebook1.title}' на реставрацию:")
# ebook1.repair()




