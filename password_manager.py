import json
from password import Password

class PasswordManager:

    def __init__(self):
        self.main_password = None
        self.passwords = []


    def set_main_password(self, main_password):
        self.main_password = main_password
    
    def get_main_password(self):
        return self.main_password

    def add_password(self, password):
        self.passwords.append(password)

    def get_passwords(self):
        return self.passwords

    def remove_password(self, password):
        # from json
        pass
