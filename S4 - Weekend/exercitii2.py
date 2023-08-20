"""
EXERCITII BONUS - OOP - EXTRA
"""

"""
1. 
a. Defineste clasa User.
Clasa User va avea urmatoarele atribute:
username (public) - se seteaza in constructor
email (public) - se seteaza in constructor
password (privat) - Nu primim atribut pentru el in constructor,
ci il initializam noi cu None (self.__password == None).

b. Implementeaza proprietatea password care va incapsula atributul privat
password.
Va avea:
- getter:
In getter verificam daca parola a fost setata (daca are valoare).
Daca are valoare, atunci vom returna ***, unde numarul de * va fi egal
cu lungimea parolei.
Daca nu e setata, atunci afisam un mesaj ca parola nu e setata.


- setter:
In setter vom verifica, inainte sa setam parola, ca aceasta indeplineste
urmatoarele conditii:
    -- are minim 10 caractere
    -- are cel putin o litera mare
Daca aceste conditii se indeplinesc atunci setam parola.
Daca nu, afisam un mesaj corespunzator pentru fiecare situatie.

c. Metode:
- Metoda login: verificam ca user-ul are atat username, email si parola.
Daca are, atunci afisam mesajul "Conectat".
Daca nu, afisam mesajul "Lipsesc credentiale de conectare. Nu va putem conecta"

d. Asigura-te ca creezi cel putin doua obiecte din clasa User.
Afiseaza toate atributele/metodele/proprietatile.
"""

class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.password = None

    @property
    def password(self):
        return self.password

    @password.getter
    def password(self):
        print('Get')
        if self.__password is not None:
            rezultat = len(self.password) * '*'
            return rezultat
        else:
            print('Parola nu este setata')

    @password.setter
    def password(self, new_password):
        print("SSSSSSSSSSSSSSSSSSSSSSSSSSSEEEEEEEEEEEEEEEETTTTTTTTTTTTTTTTTTTT")
        if new_password is not None and len(new_password) >= 10:
            for ch in new_password:
                if ch.isupper():
                   self.__pasword = new_password
                   break
            else:
                print("Ai nevoie de o litera mare")

        else:
            print("Nu are numar suficient de caractere")




obiect1 = User('flaviu','flaviudetesan@gmail.com')
print(obiect1.email)
print(obiect1.username)
# print(obiect1.password)
obiect1.password = "ikkkkkkkkkkkkkkkkk"

"""
2.
a. Defineste clasa abstracta Person.
Metode abstracte: wake_up, sleep, eat.
Metoda: describe -> afiseaza mesajul "O persoana se trezeste, mananca si doarme."

b. Defineste clasa Student.
Clasa Student implementeaza clasa abstracta Person.
Atribute in constructor: name, university, grade.
Metode describe -> afiseaza SI mesajul:
Studentul x, studiaza la universitatea y si are nota generala z.

c. Defineste clasa Employee.
Clasa Employee implementeaza cls abstracta Person.
Atribute in constructor: name, experience, salary.
Salary este un atribut privat!
Metoda describe -> afiseaza SI mesajul:
Angajatul x lucreaza de y ani.

d. Creeaza proprietatea salary care sa incapsuleze atributul privat salary.
"""