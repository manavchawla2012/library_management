from models.user import User
from repositories.user import UserRepository


class UserService:
    __instance = None
    __repository: UserRepository = None
    __user_id_counter = 1

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.__repository = UserRepository()

    def add_user(self, name):
        user = User(name=name, user_id=self.__user_id_counter)
        self.__user_id_counter += 1
        self.__repository.add_user(user)
        return user
