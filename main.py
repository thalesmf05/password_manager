from password import Password
from password_manager import PasswordManager
from storage import StorageManager 
import cli
from storage import json_path
import utils

password_manager = PasswordManager()
storage_manager = StorageManager()  


def main(password_manager):
    # check if user exists and if not create one
    cli.check_user_exists(password_manager)

    

if __name__ == "__main__":
    
    storage_manager.load_from_file(json_path)
    password_manager.passwords = storage_manager.passwords
    
    main(password_manager)
