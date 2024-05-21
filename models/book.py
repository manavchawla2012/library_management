from enum import Enum


class StatusEnum(Enum):
    AVAILABLE = 1
    BOOKED = 2


class Book:

    def __init__(self, title: str, srn: str, author: str, ):
        self.__title = title
        self.__srn = srn
        self.__status = StatusEnum.AVAILABLE
        self.__author = author

    @property
    def title(self) -> str:
        return self.__title

    @property
    def srn(self) -> str:
        return self.__srn

    @property
    def author(self) -> str:
        return self.__author

    @property
    def status(self) -> StatusEnum:
        return self.__status

    @status.setter
    def status(self, status: StatusEnum):
        self.__status = status
