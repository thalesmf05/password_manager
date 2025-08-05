from password_manager import PasswordManager
import cli

pm = PasswordManager()
def validate_main_password():
    main_password = pm.main_password
    if len(main_password) < 8: # type: ignore
        print("Main password must be at least 8 characters long. Please try again.")
        return False
    if not any(char.isupper() for char in main_password): # type: ignore
        print("Main password must contain at least one uppercase letter. Please try again.")
        return False
    if not any(char.islower() for char in main_password): # type: ignore
        print("Main password must contain at least one lowercase letter. Please try again.")
        return False
    if not any(char.isdigit() for char in main_password): # type: ignore
        print("Main password must contain at least one digit. Please try again.")
        return False
    return True

