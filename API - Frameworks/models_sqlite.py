"""Modulul care contine clasele aferente entitatilor din DB. 
Models face maparea dintre datele din DB si codul nostru Python"""

class User:
    def __init__(self, id, name, email, password, is_logged=0):
        self.id = id
        self.name = name
        self.email = email
        self.password = password   # TODO: trebuie ascunsa parola (HASH)
        self.is_logged = is_logged


    def validate(self):
        """Metoda care valideaza un User, asigurandu-se ca are field-urile potrivite, cu tipurile 
        de date potrivite, ca email-ul e valid, etc..
        return: True/False"""
        return True

    def __str__(self):
        return f"User(name={self.name}, email={self.email}, is_logged={self.is_logged})"


class Book:
    # TODO: de implementat similar cu User
    pass