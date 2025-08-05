from password_manager import PasswordManager
import cli

pm = PasswordManager()
def validate_main_password():
    main_password = pm.main_password
    if len(main_password) < 8: # type: ignore
        print("Main password must be at least 8 characters long.")
        return False
    if not any(char.isupper() for char in main_password): # type: ignore
        print("Main password must contain at least one uppercase letter.")
        return False
    if not any(char.islower() for char in main_password): # type: ignore
        print("Main password must contain at least one lowercase letter.")
        return False
    if not any(char.isdigit() for char in main_password): # type: ignore
        print("Main password must contain at least one digit.")
        return False
    return True

def get_main_password():
    while True:
        main_password = input("Enter your main password: ")
        if validate_main_password():
            return main_password
        else:
            continue