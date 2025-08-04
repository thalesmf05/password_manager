import json
from password import Password


class PasswordManager:

    def __init__(self):
        self.passwords = []

    
    def add_password(self, password):
        self.passwords.append(password)

    def get_passwords(self):
        return self.passwords