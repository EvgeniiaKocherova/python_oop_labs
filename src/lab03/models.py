from lab03.base import Book

class AudioBook(Book):
    def __init__(self, title, author, year, pages, time, reader, speed = 1.0, is_available=True, is_downloaded=False):
        if not isinstance(time, (int, float)) or time <= 0:
            raise ValueError("Длина аудиозаписи должна быть положительным числом")
        if not reader or not isinstance(reader, str):
            raise ValueError("Чтец должен быть непустой строкой")
        
        super().__init__(title, author, year, pages, is_available)
        self._is_downloaded = is_downloaded
        self._time = time
        self._reader = reader
        self._speed = speed

    def __str__(self):
        "Красивый вывод"
        if self._is_downloaded: 
            status = "скачана" 
        else: 
            status = "не скачана"
        return f'{self._title} | {self._author} | {self._year} | {status} | {self._time} мин. | {self._reader} | скорость: {self._speed}x'
    
    def download(self):
        if self._is_downloaded:
            print("Аудиокнига уже скачана")
            return False
        self._is_downloaded = True
        print("Аудиокнига скачивается")
        return True
    
    def change_speed(self, new_speed):
        "Поменять скорость воспроизвдения"
        if not isinstance(new_speed, (int, float)):
            raise TypeError("Скорость должна быть числом")
        if not (0.5 <= new_speed <= 2.0):
            raise ValueError("Скорость должна быть положительным числом от 0.5 до 2.0")  
        self._speed = new_speed
        print(f"Скорость изменена на {new_speed}x")


class EBook(Book):
    def __init__(self, title, author, year, pages, size, file, is_available=True, is_downloaded=False):

        if not isinstance(size, (int, float)) or size <= 0:
            raise ValueError("Размер файла должен быть положительным числом")
        if not (file.endswith(".pdf") or file.endswith(".epub") or file.endswith(".fb2")):
            raise ValueError("у файла неподходящее расширение")
        
        super().__init__(title, author, year, pages, is_available)
        self._is_downloaded = is_downloaded
        self._size = size
        self._file = file
        self._quotes = []

    def __str__(self):
        "Красивый вывод"
        if self._is_downloaded: 
            status = "скачана" 
        else: 
            status = "не скачана"
        return f'{self._title} | {self._author} | {self._year} | {status} | {self._size} МБ | {self._file} | цитат: {len(self._quotes)}'

    def download(self):
        "Скачивание книги(надо сделать этот метод полиморфным)"
        if self._is_downloaded:
            print("Книга уже скачана")
            return False
        self._is_downloaded = True
        print(f"Скачивается файл формата {self._file[self._file.rfind('.'):]}")
        return True

    def quote(self, text):
        "Выделение цитаты"
        if not text or not isinstance(text, str):
            raise ValueError("Цитата не может быть пустой строкой")
        self._quotes.append(text)
        print(f"Цитата: {text} была добавлена")