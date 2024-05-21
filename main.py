from service.book_service import BookService
from service.library_service import LibraryService
from service.user_service import UserService

if __name__ == '__main__':
    library_service = LibraryService()
    user_service = UserService()
    book_service = BookService()

    # Add User
    user1 = user_service.add_user("Manav")
    user2 = user_service.add_user("Dummy")

    # Add Books
    book1 = book_service.add_book("title1", "author1", 1)
    book2 = book_service.add_book("title2", "author2", 2)
    book3 = book_service.add_book("title3", "author2", 3)
    book4 = book_service.add_book("title4", "author2", 4)

    # Library Service

    print("Available Books:", library_service.available_books())

    booking = library_service.borrow_book(user1, book1.srn)
    print("Booking:", booking)

    print("Available Books:", library_service.available_books())

    # Return Book
    booking = library_service.return_book(user1, book1.srn)
    print("Book Returned")
    print("Available Books:", library_service.available_books())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
