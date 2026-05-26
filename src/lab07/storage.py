import json
from pathlib import Path
from typing import List

from lab01.model import Book
from lab03.models import AudioBook, EBook

data_dir = Path(__file__).parent.parent / "data"
default_file = data_dir / "library_data.json"


def save(books: List[Book], filepath: str = None) -> None:
    if filepath is None:
        data_dir.mkdir(parents=True, exist_ok=True)
        filepath = default_file

    data = []
    for book in books:
        item = {
            "type": book.__class__.__name__,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "pages": book.pages,
            "is_available": book.is_available
        }
        if isinstance(book, AudioBook):
            item.update(time=book.time, reader=book.reader, is_downloaded=book.is_downloaded)
        elif isinstance(book, EBook):
            item.update(size=book.size, file=book.file, is_downloaded=book.is_downloaded)
        data.append(item)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load(filepath: str = None) -> List[Book]:
    if filepath is None:
        filepath = default_file

    if not filepath.exists():
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    books = []
    for item in data:
        if item["type"] == "AudioBook":
            book = AudioBook(
                title=item["title"],
                author=item["author"],
                year=item["year"],
                pages=item["pages"],
                time=item["time"],
                reader=item["reader"],
                is_available=item["is_available"],
                is_downloaded=item.get("is_downloaded", False)
            )
        elif item["type"] == "EBook":
            book = EBook(
                title=item["title"],
                author=item["author"],
                year=item["year"],
                pages=item["pages"],
                size=item["size"],
                file=item["file"],
                is_available=item["is_available"],
                is_downloaded=item.get("is_downloaded", False)
            )
        else:
            book = Book(
                title=item["title"],
                author=item["author"],
                year=item["year"],
                pages=item["pages"],
                is_available=item["is_available"]
            )
        books.append(book)
    return books