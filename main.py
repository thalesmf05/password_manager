from password import Password
from password_manager import PasswordManager

p = PasswordManager()

eu = Password("gmail", "eu@gmail.com", "1")
ela = Password("hotmail", "ela@hotmail.com.br", "ela_linda")

p.add_password(eu)
p.add_password(ela)

#protected_password = eu.protected_password()

#print(protected_password)

print(eu)