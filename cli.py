from password_manager import PasswordManager
import utils
import cli


def get_new_main_password(password_manager):
    while True:
        main_password = input("Enter your main password: ")
        if utils.is_password_strength(main_password)[0] is True:
            return main_password
        else:
            print(utils.is_password_strength(main_password)[1])
            continue

def check_user_exists(password_manager):
    if utils.user_exists(password_manager):
        print("Welcome back!")
    else:
        cli.create_user(password_manager)
        print("Your account has been created successfully!")

def create_user(password_manager):
    print("Welcome to my python password manager!!")
    main_password = get_new_main_password(password_manager)
    password_manager.set_main_password(main_password)
    print("Your main password has been set successfully!")
