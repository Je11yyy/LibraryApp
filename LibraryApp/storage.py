from abc import ABC, abstractclassmethod
class Storage(ABC):
    """Class for Storage"""
    @abstractclassmethod
    def save():
        pass
    @abstractclassmethod
    def load():
        pass

class Storage_libr(Storage):
    """Class for Books in Storage"""
    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def save(library):
        with open(file=library.file, mode='a') as file:
            file.write(library.libr)
        library.libr = ""
        print("Saved successfully")

    def load(self):
        content = ""
        with open(file=self.filename, mode='r') as file:
            for line in file:
                content += line
        print("Loaded successfully")
        return content
    
class Storage_users(Storage):
    """Class for Users in Storage"""
    @staticmethod
    def save(user):
        from models import Admin, Reader
        if isinstance(user, Admin):
            with open(file="list_admins.txt", mode='a') as file:
                file.write(user.name +' -- '+ user.library +'\n')
            print("Saved successfully")

        elif isinstance(user, Reader):
            with open(file="list_users.txt", mode='a') as file:
                file.write(f"{user.name} --- {user.inventory}\n")
            print("Saved successfully")
    
    def load(self):
        list = []
        with open(file="list_users.txt", mode='r') as file:
            for line in file:
                part = line.split(' --- ')
                line = str(part[1])
                part = line.split("'")
                line = str(part[1])
                list.append(line)
        print("Loaded successfully")
        return list
