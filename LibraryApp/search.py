from abc import ABC, abstractclassmethod
from models import Types
import json


class SearchStrategy(ABC):
    """Class for Search Strategy"""
    @abstractclassmethod
    def search():
        pass

class TitleSearch(SearchStrategy):
    @staticmethod
    def search(title: str, library: "Library"):
        try:
            with open(file=library.file, mode='r') as file:
                books = json.load(file)
            for book in books:
                if book["name"] == title:
                    return book
            return None
        except:
            return None

class GenreSearch(SearchStrategy):
    @staticmethod
    def search(genre, library):
        try:
            with open(file=library.file, mode='r') as file:
                books = json.load(file)
            list = []
            for book in books:
                if book["genre"] == genre:
                    list.append(book)
            return list
        except:
            return None

class TypeofBook(SearchStrategy):
    @staticmethod
    def search(typeof : Types, library):
        if isinstance(typeof, Types):
            try:
                with open(file=library.file, mode='r') as file:
                    books = json.load(file)
                list = []
                for book in books:
                    if book["type"] == typeof:
                        list.append(book)
                return list
            except:
                return None
