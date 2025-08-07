import json
from password import Password
from password_manager import PasswordManager

json_path = r"C:\Users\Laptops 2024\Desktop\projects\python\password_manager\data\passwords.json"
class StorageManager:
    def __init__(self):
        self.passwords = []

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            password_dict = [password.to_dict() for password in self.passwords]
            json.dump(password_dict, f, indent=4)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f: 
                password_dicts = json.load(f)
                self.passwords = [Password.from_dict(pd) for pd in password_dicts]
        except FileNotFoundError:
            self.passwords = []

