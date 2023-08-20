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

import math


class Cerc:

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f"Acest cerc are raza de {self.raza} cm si culoarea {self.culoare}")

    def aria(self):
        aria_cerc = self.raza * self.raza * math.pi
        return aria_cerc

    def diametru(self):
        diametru_cerc = 2 * self.raza
        return diametru_cerc

    def circumferinta(self):
        circumferinta = self.raza * 2 * math.pi
        return circumferinta


cerc1 = Cerc(2, 'rosu')
print(cerc1)
cerc1.descrie_cerc()
print(cerc1.aria())
print(cerc1.diametru())
print(cerc1.circumferinta())

cerc2 = Cerc(5, 'galben')
print(cerc2)
cerc2.descrie_cerc()
print(cerc2.aria())
print(cerc2.diametru())
print(cerc2.circumferinta())


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

class Dreptunghi:

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f"Acesta este un dreptunghi cu dimensiunile: {self.lungime}, {self.latime} si culoarea {self.culoare}")

    def arie(self):
        arie_dreptunghi = self.latime * self.lungime
        return arie_dreptunghi

    def perimetru(self):
        perimetru_dreptunghi = self.latime * 2 + self.lungime * 2
        return perimetru_dreptunghi

    def schimba_culoare(self, culoare_noua):
        self.culoare = culoare_noua
        self.descrie()


dreptunghi1 = Dreptunghi(5, 2, 'albastru')
dreptunghi1.descrie()
print(dreptunghi1.arie())
print(dreptunghi1.perimetru())
dreptunghi1.schimba_culoare('galben')

dreptunghi2 = Dreptunghi(10, 4, 'portocaliu')
dreptunghi2.descrie()
print(dreptunghi2.arie())
print(dreptunghi2.perimetru())
dreptunghi2.schimba_culoare('alb')



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
class Angajat:

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f"Angajatul {self.nume} {self.prenume} are salariul de {self.salariu}")

    def nume_complet(self):
        nume_complet = self.nume + ' ' + self.prenume
        return nume_complet

    def salariu_lunar(self):
        print(f"Salariul lunar al acestui angajat este {self.salariu}")

    def salariu_anual(self):
        salariu_anual = 12 * self.salariu
        print(f"Salariul anual al acestui angajat este {salariu_anual}")

    def marire_salariu(self, procent):
        self.salariu = self.salariu + self.salariu * procent / 100
        return self.salariu


angajat1 = Angajat("Pop", "Maria", 10000)
angajat1.descrie()
print(angajat1.nume_complet())
angajat1.salariu_lunar()
angajat1.salariu_anual()
print(angajat1.marire_salariu(25))


angajat2 = Angajat("Pop", "Ion", 11000)
angajat2.descrie()
print(angajat2.nume_complet())
angajat2.salariu_lunar()
angajat2.salariu_anual()
print(angajat2.marire_salariu(10))

"""
4. Clasa Cont
   Atribute: iban, titular_cont, sold
   Constructor pentru toate atributele
   Metode:
afisare_sold() - Titularul x are în contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
"""

class Cont:

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.")

    def debitare_cont(self, suma):
        if suma <= self.sold:
            self.sold -= suma
        else:
            print("Fonduri insuficiente!")

    def creditare_cont(self, suma):
        self.sold += suma


cont1 = Cont('RO54BTRLRONCRT000000', 'Pop Ana', 20000)
cont1.afisare_sold()
print(cont1.sold)
cont1.debitare_cont(1000)
print(cont1.sold)
cont1.creditare_cont(1000)
print(cont1.sold)

cont2 = Cont('RO80BTRLRONCRT111111', 'Pop Alina', 500)
cont2.afisare_sold()
print(cont2.sold)
cont2.debitare_cont(4000)
print(cont2.sold)
cont2.creditare_cont(1000)
print(cont2.sold)



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

# pip install tabulate
from datetime import date
from tabulate import tabulate


class Factura:
    seria = 123456

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def calc_total(self):
        return self.pret_buc * self.cantitate

    def genereaza_factura(self):
        print(tabulate([[self.nume_produs, self.cantitate, self.pret_buc, self.calc_total(), date.today()]],
                       headers=['Produs', 'Cantitate', 'Pret Buc', 'Total', 'Data']))


factura1 = Factura(1, 'birou', 5.00, 100)
factura1.genereaza_factura()

factura2 = Factura(2, 'scaun', 3.00, 45)
factura2.schimba_cantitatea(4.00)
factura2.schimba_pretul(50)
factura2.schimba_nume_produs('scaun de masaj')
factura2.genereaza_factura()