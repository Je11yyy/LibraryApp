from abc import ABC, abstractclassmethod
import json

class Storage_save(ABC):
    @abstractclassmethod
    def save():
        pass

class Storage_load(ABC):
    @abstractclassmethod
    def load():
        pass


class Storage_libr(Storage_save, Storage_load):
    """Class for Books in Storage"""
    def __init__(self, filename):
        self.filename = filename

    def save(self, library):
        with open(file=self.filename, mode='w') as file: 
            json.dump(library.libr, file, indent=4)
        library.libr = []
        print("Saved successfully for library")

    def load(self):
        try:
            with open(file=self.filename, mode='r') as file:
                books = json.load(file)
        except:
            return []
        print("Loaded successfully for library")
        return books
    
    
class Admin_Storage(Storage_save):
    def __init__(self):
        self.filename = "admins.json"

    def save(self, user):
        try:
            with open(file=self.filename, mode='r') as file:
                admins = json.load(file)
        except:
            admins = []

        admins.append({
            "name": user.name,
            "library": str(user.library)
        })

        with open(file=self.filename, mode='w') as file: 
            json.dump(admins, file, indent=4)   
        print("Saved successfully for admin")                          

class Reader_Storage(Storage_save, Storage_load):
    def __init__(self):
        self.filename = "readers.json"

    def save(self, user):
        try:
            with open(file=self.filename, mode='r') as file:
                readers = json.load(file)
        except:
            readers = []
        # ЕСЛИ ЧИТАТЕЛЬ ЗАШЕЛ НА САЙТ К ПРИМЕРУ, 
        # ЗАРЕГАЛСЯ, НО НЕ КУПИЛ КНИГУ --> ТО ЕГО НЕТ СМЫСЛА ДЕРЖАТЬ В БАЗЕ
        if user.inventory == []:
            return None
        
        readers.append({
            "name": user.name,
            "inventory": user.inventory
        })

        with open(file=self.filename, mode='w') as file:  
            json.dump(readers, file, indent=4)
        user.inventory = []
        print("Saved successfully for reader")

    def load(self, name):
        try:
             with open(file=self.filename, mode='r') as file:
                readers = json.load(file)
        except:
            return []
        
        for reader in readers:
            if reader['name'] == name:
                print("Loaded successfully for reader")
                return reader["inventory"]
        return []
