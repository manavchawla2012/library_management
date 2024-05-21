from typing import List

from models.book import Book, StatusEnum
from repositories.book import BookRepository


class BookService:
    __instance = None
    __repository: BookRepository = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            cls.__repository = BookRepository()
        return cls.__instance

    def add_book(self, title, author, srn):
        book = Book(title=title, author=author, srn=srn)
        self.__repository.add_book(book)
        return book

    def remove_book(self, srn):
        book = self.__repository.get_book_by_srn(srn)
        self.__repository.remove_book(book)

    def search_book_by_title(self, title: str) -> Book:
        return self.__repository.get_book_by_title(title)

    def search_books_by_author(self, author: str) -> List[Book]:
        return self.__repository.get_books_by_author(author)

    def search_books_by_srn(self, srn: str) -> Book:
        return self.__repository.get_book_by_srn(srn)

    def borrow_book(self, book: Book):
        return self.__repository.update_book_status(StatusEnum.BOOKED, book)

    def return_book(self, book: Book):
        return self.__repository.update_book_status(StatusEnum.AVAILABLE, book)

    def available_books(self) -> List[Book]:
        return self.__repository.available_books()
