from typing import List

from models.user import User


class UserRepository:
    __instance = None
    __initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True
        self.__users: List[User] = []

    def add_user(self, user: User):
        self.__users.append(user)
