from model import Book

print("===Создание книг===")
#Демонстрация создания книг
book1 = Book("Вишневый сад", "Антон Павлович Чехов", 1904, 89, 200)
book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 950, False)
book3 = Book("Война и мир", "Лев Толстой", 1867, 1300, 1200)

print(book1)
print(book2)
print(book3)
print("            ")

print("===Разные выводы===")
#Демонстрация разных выводов
print(str(book1))
print(repr(book1))
print("            ")

print("===Сравнение книг===")
#Демонстрация сравнения книг
book4 = Book("Вишневый сад", "Антон Павлович Чехов", 1904, 89, 200)
print(book1 == book2)
print(book1 == book1)
print(book1 == book4)
print("            ")

print("===Демонстрация книг без цены===")
book5 = Book("Бесплатная книга", "автор", 2020, 50, None)
print(book5)

print("===Геттеры===")
#Демонстрация геттеров
print(book1.title)
print(book1.author)
print(book1.year)
print(book1.price)
print(book1.pages)
print("            ")

print("===Сеттеры===")
#Демонстрация сеттеров
print(f"Старая цена book1: {book1.price} руб.")
book1.price = 370
print(f"Новая цена book1: {book1.price} руб.")

print(f"Старый год book1: {book1.year}")
book1.year = 2024
print(f"Новый год book1: {book1.year}")

print(f"Книга после изменений: {book1}")
print("            ")

print("===Атрибут класса===")
#Демонстрация атрибутов класса
print(Book._catalog_of_books)
print(book1._catalog_of_books)
print(len(Book._catalog_of_books))
print("       ")

print("===Бизнес-методы===")
print(f"Книга до выдачи: {book2}")  

print("Пытаемся выдать book2...")
book2.give_book()  

print(f"Книга до выдачи: {book3}")  
print("Выдаем book3...")
book3.give_book()
print(f"Книга после выдачи: {book3}")

print("Возвращаем book3...")
book3.return_book()
print(f"Книга после возврата: {book3}")
print("            ")

print("===Метод класса show_catalog===")
Book.show_catalog()
print("            ")


print("===Обработка ошибок при создании===")
try:
    bad_book = Book("", "Автор", 2000, 100, 500)
except ValueError as e:
    print(f"Ошибка при пустом названии: {e}")

try:
    bad_book = Book("Название", "Автор", 1400, 100, 500)  # год меньше 1450
except ValueError as e:
    print(f"Ошибка при старом годе: {e}")

try:
    bad_book = Book("Название", "Автор", 2000, -50, 500)  # отрицательные страницы
except ValueError as e:
    print(f"Ошибка при страницах: {e}")
print("            ")

try:
    bad_book = Book("Название", "", 1600, 1000, 50)
except ValueError as e:
    print(f"Ошибка при пустом авторе: {e}")


print("===Демонстрация поведения, зависящего от состояния===")
print(f"Книга до выдачи: {book3}")
print("Пытаемся изменить цену выданной книги:")
try:
    book3.price = 500
    book3.give_book()  # выдаем книгу
    print("Книга выдана, теперь пробуем изменить цену:")
    book3.price = 600  # должно вызвать ошибку
except ValueError as e:
    print(f"❌ Ошибка: {e}")

print("\n===Демонстрация метода реставрации===")
book1.repair()  # книга в наличии - можно реставрировать
book3.repair()  # книга выдана - нельзя реставрировать

