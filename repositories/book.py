from typing import Dict, List

from models.book import Book, StatusEnum


class BookRepository:
    __instance = None
    __initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)

        return cls.__instance

    def __init__(self):
        if self.__initialized: return
        self.__initialized = True
        self.__book_title_mapping: Dict[str, Book] = {}
        self.__book_id_mapping: Dict[str, Book] = {}

    def add_book(self, book):
        self.__book_title_mapping[book.title] = book
        self.__book_id_mapping[book.srn] = book
        return book

    def remove_book(self, book):
        del self.__book_id_mapping[book.srn]
        del self.__book_title_mapping[book.title]

    def get_book_by_title(self, title):
        return self.__book_title_mapping.get(title)

    def get_book_by_srn(self, srn):
        return self.__book_id_mapping.get(srn)

    def get_books_by_author(self, author) -> List[Book]:
        return list(filter(lambda book: book.author == author, self.__book_title_mapping.values()))

    def update_book_status(self, status: StatusEnum, book: Book) -> Book:
        book.status = status
        return book

    def available_books(self) -> List[Book]:
        return list(filter(lambda x: x.status == StatusEnum.AVAILABLE, self.__book_title_mapping.values()))
