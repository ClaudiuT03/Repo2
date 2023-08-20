# Partea 1 - Setup, Variabile, Tipuri de date
for i in range(4,0,-2):
    print(i)
# Exerciții - studiu în workshopul de weekend
prop = 'Ana are mere'
print(prop[4:9])
# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
#  o variabila este o "cutiuta" cu unn continut(valoare)

# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
# string_var ="Narcisa"
# int_var = 10
# float_var = 15.6
# bool_var = True
# Observație: Valorile vor fi alese de tine după preferințe.

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
# print(type(string_var))
# print(type(int_var))
# print(type(float_var))
# print(type(bool_var))

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
# print(round(float_var))
# float_var = round(float_var)
# Verifică tipul acesteia.
# print(type(float_var))

# 5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.
# print(string_var)
# print(f" acesta este un nr int {int_var}")
# print(f" acesta este un nr float {float_var}")
# print(f" acesta este un nr bool {bool_var}")

# 6. Citește de la tastatură:
# numele;
# nume = input("Numele:")
# prenumele.
# prenume = input("Prenume:")
# x = len(nume)+ len(prenume)
#     Afișează: 'Numele complet are x caractere'.
# print("Numele complet are" + str(x) + "caractere")

# 7. Citește de la tastatură:
# lungimea;
# lungimea = input("Lungimea:")
# lățimea.
# latimea = input("Latimea:")
#    Afișează: 'Aria dreptunghiului este x'.
# aria = float(lungimea) * float(latimea)
# print(f'aria dreptunghiului este str({aria})')

# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# afișează de câte ori apare cuvântul 'the';
# Printează rezultatul.
# coral = "Coral is either the stupidest animal or the smartest rock"
# print(coral.count("the"))

# 9. Același string:
# Folosește un assert ca să verifici dacă acest string conține doar numere.
# assert coral.isnumeric()
# str1 = "Coral is either the stupidest animal or the smartest rock"
# assert str1.isnumeric()

# 10. Exercițiu:
# citește de la tastatură un string de dimensiune impară;
# afișează caracterul din mijloc.

# str1 = input("Introduceti un string de dimensiune impara ")
#
# # print(str1[2])
#
# y = len(str1)
# if y % 2 == 1:
#     # print(str1[int(y/2)])
#     print(str1[y//2])

# 11. Folosind o singură linie de cod :
# citește un string de la tastatură (ex: 'alabala portocala');
# salvează fiecare cuvânt într-o variabilă;
# printează ambele variabile pentru verificare.

# a, b = input("Introdu un text: ").split()
# print(a)
# print(b)


# 12. Exercițiu:
# citește un string de la tastatură (ex: alabala portocala);
# salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
# capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.

# string1 = input("Introduceti un text")
# first_char = string1[0]
# print(first_char)
# str2 = string1[1:-1].replace(first_char,first_char.upper())
# print(string1)
# print(str2)
# print(first_char + str2 + string1[-1])

# 13. Exercițiu:
# citește un user de la tastatură;
# citește o parolă;
# afișează: 'Parola pt user x este ***** și are x caractere';
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.

# eg: parola abc => ***
#       parola abcd => ****
#
# username = input("User name:")
# parola = input("Parola:")
# x = len(parola)
# parlent = x * '*'
# print(f'Parola pt {username} este {parlent} si are {x} caractere')