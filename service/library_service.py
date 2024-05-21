from datetime import datetime
from typing import List

from models.book import Book, StatusEnum
from models.user import User
from service.book_service import BookService
from service.user_service import UserService


class Booking:

    def __init__(self, book_srn, user_id):
        self.__book_srn = book_srn
        self.__user_id = user_id
        self.__created_on = datetime.now()
        self.__returned_on = None

    @property
    def book_srn(self):
        return self.__book_srn

    @property
    def user_id(self):
        return self.__user_id

    @property
    def created_on(self):
        return self.__created_on

    @property
    def returned_on(self):
        return self.__returned_on

    def book_returned(self):
        self.__returned_on = datetime.now()


class LibraryService:
    __instance = None
    __initialised = False

    __book_service = None
    __user_service = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            cls.__book_service = BookService()
            cls.__user_service = UserService()

        return cls.__instance

    def __init__(self):
        if self.__initialised:
            return
        self.__bookings: List[Booking] = []

    def __can_borrow_book(self, book: Book) -> bool:
        return book.status == StatusEnum.AVAILABLE

    def borrow_book(self, user: User, srn) -> Booking | None:
        book = self.__book_service.search_books_by_srn(srn)
        if not book:
            return
        if not self.__can_borrow_book(book):
            return
        booking = Booking(
            user_id=user.user_id,
            book_srn=book.srn
        )
        self.__bookings.append(booking)
        self.__book_service.borrow_book(book)
        return booking

    def return_book(self, user: User, srn: str) -> Booking | None:
        booking = None
        for tb in self.__bookings:
            if tb.book_srn == srn and tb.user_id == user.user_id:
                booking = tb
                break
        if not booking:
            return
        book = self.__book_service.search_books_by_srn(srn)
        self.__book_service.return_book(book)
        booking.book_returned()
        return booking

    def available_books(self) -> List[Book]:
        return self.__book_service.available_books()
