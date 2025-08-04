

class Password:

    def __init__(self, web_site, user, password):
        self.web_site = web_site
        self.user = user
        self.password = password

    def __str__(self):
        return f"Site: {self.web_site} | User: {self.protected_user()} | Password: {self.protected_password()}"

    def change_user(self, new_user):
        self.user = new_user


    def change_password(self, new_password):
        self.password = new_password
    
    def protected_password(self): #ok
        return "*"*len(self.password)
    
    def protected_user(self): #ok
        user = self.user.split("@")
        str_user = f"{"*"*len(user[0])}{user[1]}"
        return str_user

    def to_dict(self):
        return{
            "web_site": self.web_site,
            "user": self.user,
            "password": self.password
        }
    
    @classmethod
    def from_dict(cls, data):
        web_site = data["web_site"]
        user = data["user"]
        password = data["password"]
        return cls(web_site, user, password)
