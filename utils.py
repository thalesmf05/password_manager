from password_manager import PasswordManager
import cli
from main import password_manager
from typing import Tuple


def user_exists(password_manager):
    if password_manager.get_main_password():
        return True
    return False

def is_password_strength(password: str) -> Tuple[bool, str]:

    if len(password) < 8:
        return (False, "Main password must be at least 8 characters long. Please try again.")
    if not any(char.isupper() for char in password):
        return (False, "Main password must contain at least one uppercase letter. Please try again.")
    if not any(char.islower() for char in password):
        return (False, "Main password must contain at least one lowercase letter. Please try again.")
    if not any(char.isdigit() for char in password):
        return (False, "Main password must contain at least one digit. Please try again.")
    return (True, "Main password is strong.")
