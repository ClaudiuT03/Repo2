"""
PARTEA 2 - OOP: Clase & Obiecte
"""

"""
1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria
diametru()
circumferinta()
"""
# class Cerc:
#     def init(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descrie_cerc(self):
#         print(f"Cercul are raza {self.raza} si culoarea {self.culoare}.")
#
#     def calculeaza_arie(self):
#         arie = 3.14 * self.raza ** 2
#         return arie
#
#     def diametru(self):
#         diametru = 2 * self.raza
#         return diametru
#
#     def circumferinta(self):
#         circumferinta = 3.14 * 2 * self.raza
#         return circumferinta
#
# cerc1 = Cerc(5, "portocaliu")
# print(cerc1.raza)
# print(cerc1.culoare)
# cerc1.descrie_cerc()
# print(cerc1.calculeaza_arie())
# print(cerc1.diametru())
# print(cerc1.circumferinta())
#
# cerc2 = Cerc (9, "verde")
# print(cerc2.raza)
# print(cerc2.culoare)
# cerc2.descrie_cerc()
# print(cerc2.calculeaza_arie())
# print(cerc2.diametru())
# print(cerc2.circumferinta())
"""
2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().
"""
# class Dreptunghi:
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descrie(self):
#         print(self.culoare)
#
#     def calculeaza_aria(self):
#        aria = self.latime * self.lungime
#        print(aria)
#        return aria
#
#     def perimetrul(self):
#         perimetru = 2*(self.lungime + self.latime)
#         print(perimetru)
#         return perimetru
#
#     def schimba_culoarea(self, noua_culoare):
#         self.culoare = noua_culoare
#         self.descrie()
#         print(f"noua culoare {noua_culoare}")
#
#
# dreptunghi1 = Dreptunghi(latime=2,lungime=6,culoare='rosu')

# dreptunghi1.calculeaza_aria()
# dreptunghi1.perimetrul()
# dreptunghi1.descrie()
# dreptunghi1.schimba_culoarea('verde')
# print(dreptunghi1.latime)
# print(dreptunghi1.lungime)
# print(dreptunghi1.culoare)

# dreptunghi2 = Dreptunghi(4,5,'alb')
#
# dreptunghi2.calculeaza_aria()
# dreptunghi2.perimetrul()
# dreptunghi2.descrie()
# dreptunghi2.schimba_culoarea('albastru')
# print(dreptunghi2.latime)
# print(dreptunghi2.lungime)
# print(dreptunghi2.culoare)
"""
3. Clasa Angajat
     Atribute: nume, prenume, salariu
     Constructor pentru toate atributele
     Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
"""
# class Angajat:
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie(self):
#         print(self.nume)
#         print(self.prenume)
#         print(self.salariu)
#
#     def nume(self):
#         return f"nume:{self.nume} prenume:{self.prenume}"
#     def salariu_lunar(self):
#         return f"salariul lunar{self.salariu}"
#     def salariu_anual(self):
#         return self.salariu *12




"""
4. Clasa Cont
   Atribute: iban, titular_cont, sold
   Constructor pentru toate atributele
   Metode:
afisare_sold() - Titularul x are în contul y suma de n lei
debitare_cont(suma) soldul - suma data ca param
creditare_cont(suma) soldul + suma data ca param
"""
# class Card:
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#
#     def afisare_sold(self):
    #     print(f"Titularul: {self.titular_cont} are in contul:{self.iban} suma de {self.sold} lei")
    # def debitare_cont(self,suma):
    #     debitare = self.sold - suma
    #     print(f"In cont au mai ramas {debitare} lei")
    #     return debitare
    # def creditare_cont(self,suma):
    #     creditare = self.sold + suma
    #     print(f"Aveti acum suma de {creditare} lei")
    #     return creditare

# client1 = Card(12345, 'Vasile Ion', 268)
# client1.afisare_sold()
# client1.debitare_cont(200)
# client1.creditare_cont(200)
#
# client2 = Card(12345678, 'Ionel Grigore', 675)
# client2.afisare_sold()
# client2.debitare_cont(100)
# client2.creditare_cont(198)
"""
5. Clasa Factură
     Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
     Constructor: toate atributele, fără serie
     Metode:
schimbă_cantitatea(cantitate)
schimbă_prețul(pret)
schimbă_nume_produs(nume)
generează_factura() - va printa tabelar dacă reușiți

Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total
Telefon |      7       |       700       | 49000

Indiciu pentru dată: https://www.geeksforgeeks.org/get-current-date-using-python/
"""
# from datetime import date
# class Factura:
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.cantitate = cantitate
#         self.pret = pret_buc
#         self.nume = nume_produs
#         self.numar = numar
#
#     def schimba_cantitatea(self, cantitate):
#         self.cantitate = cantitate
#         print(cantitate)
#
#     def schimba_pretul(self, pret):
#         self.pret = pret
#         print(pret)
#
#     def schimba_nume_produs(self, nume):
#         self.nume = nume
#         print(nume)
#
#     def genereaza_factura(self):
#         total = self.cantitate* self.pret
#         serie = "xazvxca"
#         today = date.today()
#         print(f"Factura seria {serie} numar {self.numar} \n Data: {today} \n {self.nume} | {self.cantitate} | {self.pret} | {total}")
#
#
# f = Factura(1, "kito", 4, 20)
# f.schimba_pretul(200)
# f.schimba_cantitatea(5)
# f.schimba_nume_produs("Kiko")
# f.genereaza_factura()





