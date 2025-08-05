from math import e
from password_manager import PasswordManager
import password_manager
from utils import validate_main_password

pm = PasswordManager()
def get_main_password():
    while True:
        main_password = input("Enter your main password: ")
        if validate_main_password() is True:
            return main_password
        else:
            continue 


def new_user():
    print("Welcome to my python password manager!!")
    user_name = input("Enter your name: ")
    main_password = get_main_password()
    

