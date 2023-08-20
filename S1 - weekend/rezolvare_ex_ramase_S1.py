"""
14.      x, y, z (int)
Afișează care este cel mai mare dintre ele?
"""
x = int(input("Numarul x: "))
y = int(input("Numarul y: "))
z = int(input("Numarul z: "))

if x >= y and x >= z:
    print(f'{x} este cel mai mare numar.')
elif y >= x and y >= z:
    print(f'{y} este cel mai mare numar.')
else:
    print(f'{z} este cel mai mare numar.')

"""
15.
x, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
"""
x = int(input("Unghi 1: "))
y = int(input("Unghi 2: "))
z = int(input("Unghi 3: "))
if x + y + z == 180 and x > 0 and y > 0 and z > 0:
    print("Triunghiul este valid.")
else:
    print("Triunghiul NU este valid.")

"""
16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
Citește de la tastatură un int x
Afișează stringul fără ultimele x caractere
Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
"""
my_str = 'Coral is either the stupidest animal or the smartest rock'

x = int(input("Valoare x: "))

"""
b. Afișează stringul fără ultimele x caractere.
"""

print(my_str[:-x])

"""
17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
"""
str_nou = my_str[:5] + my_str[-5:]
print(f"str nou: {str_nou}")

"""
18. Același string.
Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
output: 'Coral is either the stupidest animal or the smartest'
"""
start_i = my_str.index("rock")
print(start_i)
print(my_str[:start_i])

"""
19. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
"""
import random

number = random.randint(0, 9)
user_number = int(input("Alege un numar: "))
if user_number < number:
    print(f"Ai pierdut! Ai ales un numar mai mic. Ai ales {user_number} dar era {number}.")
elif user_number > number:
    print(f"Ai pierdut! Ai ales un numar mai mare. Ai ales {user_number} dar era {number}.")
else:
    print(f"Ai ghicit. Felicitari! Ai ales {user_number} si zarul a fost {number}.")

"""
20.  Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
"""

str_input = input("Introduceti un string: ")
assert str_input[0].lower() == str_input[-1].lower()

"""
21. Având stringul '0123456789'
Afișează doar numerele pare
Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)
"""
str_numbers = '0123456789'

# printam numerele pare
print(str_numbers[0::2])

# printam numerele impare
print(str_numbers[1::2])
