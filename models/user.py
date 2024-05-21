class User:

    def __init__(self, name, user_id):
        self.__name = name
        self.__user_id = user_id

    @property
    def name(self):
        return self.__name

    @property
    def user_id(self):
        return self.__user_id
