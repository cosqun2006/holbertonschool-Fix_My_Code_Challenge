#!/usr/bin/python3
"""
User class
"""


class User():
    """ Documentation """

    def __init__(self):
        """ Documentation """
        self.__password = None

    @property
    def password(self):
        """ Documentation """
        return self.__password

    @password.setter
    def password(self, value):
        """ Documentation """
        if type(value) is str:
            self.__password = value

    def is_valid_password(self, password):
        """ Documentation """
        if password is None or type(password) is not str:
            return False
        if self.__password is None:
            return False
        return self.__password == password


if __name__ == "__main__":
    print("Test User")
    user = User()
    user.password = "Documentation"
    if not user.is_valid_password("Documentation"):
        print("is_valid_password should return True if it's the right password")
