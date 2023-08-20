"""

OOP - advance

Exerciții - studiu în workshopul de weekend

1. ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’
"""
from abc import ABC, abstractmethod

class FormaGeometrica:
    Pi = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print("Cel mai probabil am colturi")

forma1 = FormaGeometrica()
#
# forma1.descrie()
"""

2. INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
"""
class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    # @abstractmethod
    def aria(self):
        aria = self.__latura * self.__latura
        return aria

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print("Get")
        return self.__latura

    @latura.setter
    def latura(self, value):
        print("Set")
        self.__latura = value

    @latura.deleter
    def latura(self):
        print("Delete")
        self.__latura = 0

# patrat1 = Patrat(55)  getter
# print(patrat1.aria()) print valoare aria
# patrat1.descrie()   print met descrie
# print(patrat1.latura) getter
# patrat1.latura = 11  setter
# print(patrat1.latura) getter
# del patrat1.latura delleter
# print(patrat1.latura)
"""
3. Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
"""
class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        aria = self.Pi * (self.raza * self.raza)
        return aria

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print("Get")
        return self.__raza

    @raza.setter
    def raza(self, value):
        print("Set")
        self.__raza = value

    @raza.deleter
    def raza(self):
        print("Delete")
        self.__raza = 2




# cerc1 = Cerc(3)
# print(cerc1.aria())
# cerc1.descrie()
# print(f'getter {cerc1.raza}')
# cerc1.raza = 11
# print(f'getter dupa setter {cerc1.raza}')
# print(cerc1.aria())
# del cerc1.raza
# print(f'getter dupa deletter {cerc1.raza}')
# print(cerc1.aria())
# cerc1.descrie()

"""
4. POLYMORPHISM 
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
"""


def descrie(self):
    print("Eu nu am colturi!")

"""
5. Creează un obiect de tip Pătrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
"""
patrat1 = Patrat(55)
print(patrat1.aria())
patrat1.descrie()
cerc1 = Cerc(3)
print(cerc1.aria())
cerc1.descrie()

"""
6. Actualizează proiectul pe github facand un push la noul cod
În Folderul de teme ajunge să pui doar linkul cu proiectul tău public

Sa avem github-ul instalat și să ne incarcam în acesta fișierele python lucrate în workshop-urile de weekend.
"""
