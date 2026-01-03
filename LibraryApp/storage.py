from abc import ABC, abstractclassmethod
class Storage(ABC):
    """Class for Storage"""
    def save():
        pass
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
        print("Saved successfully for library")

    def load(self):
        content = ""
        with open(file=self.filename, mode='a+') as file:
            file.seek(0)
            for line in file:
                content += line
            print("Loaded successfully for library")
            return content
    
class Load_reader(Storage):
    """Class for Users in Storage"""
    def load(self):
         with open(file="list_readers.txt", mode='a+') as file:
            file.seek(0)
            list = []
            for line in file:
                part = line.split(' --- ')
                line = str(part[1])
                part = line.split("'")
                line = str(part[1])
                list.append(line)
            print("Loaded successfully for reader")
            return list

class Save_admin(Storage):
    @staticmethod            
    def save(user):
        with open(file="list_admins.txt", mode='a') as file: 
            file.write(f"{user.name} --- {user.library}\n")
        print("Saved successfully for admin")                          

class Save_reader(Storage):
    @staticmethod
    def save(user):
        with open(file="list_readers.txt", mode='a') as file:  
            file.write(f"{user.name} --- {user.inventory}\n")
        user.inventory = []
        print("Saved successfully for reader")                           

















