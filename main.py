from password import Password
from password_manager import PasswordManager
from storage import StorageManager 
import cli

cli.new_user()


eu = Password("gmail", "eu@gmail.com", "1")
ela = Password("hotmail", "ela@hotmail.com.br", "ela_linda")

p = PasswordManager()
p.add_password(eu)
p.add_password(ela)
storage = StorageManager()
json_path = "passwords.json"  # Define the path to save the JSON file
storage.save_to_file(json_path)

storage.load_from_file(json_path)
print(storage.passwords)  # This will print the loaded passwords

