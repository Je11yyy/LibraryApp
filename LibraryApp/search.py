from abc import ABC, abstractclassmethod
from library_core import Library
from models import Types


class SearchStrategy(ABC):
    """Class for Search Strategy"""
    @abstractclassmethod
    def search():
        pass

class TitleSearch(SearchStrategy):
    @staticmethod
    def search(title, library : Library):
        title = f"{title.center(18)}"
        with open(file=library.file, mode='r') as file:
            lines = file.readlines()
            for line in lines:
                part = line.split('|')
                if part[2] == title:
                    return line
                
class GenreSearch(SearchStrategy):
    @staticmethod
    def search(genre, library : Library):
        genre = f"{genre.center(10)}"
        with open(file=library.file, mode='r') as file:
            lines = file.readlines()
            list = []
            for line in lines:
                part = line.split('|')
                if part[3] == genre:
                    list.append(line)
            return list

class TypeofBook(SearchStrategy):
    @staticmethod
    def search(type : Types, library : Library):
        if isinstance(type, Types):
            type = f"{type.center(13)}"
            with open(file=library.file, mode='r') as file:
                lines = file.readlines()
                list = []
                for line in lines:
                    part = line.split('|')
                    if part[4] == type:
                        list.append(line)
                return list