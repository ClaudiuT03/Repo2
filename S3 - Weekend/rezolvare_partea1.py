"""
PARTEA 1 - FUNCTII

Exerciții - studiu în workshopul de weekend

Pentru toate exercițiile: Apelați funcția de cel puțin 2 ori cu valori diferite pentru a testa.
Dacă funcția are return, printează răspunsul.
"""

"""
1. Funcție care să calculeze și să returneze suma a două numere.
"""

def calculate_sum(a, b):
    return a + b


sum1 = calculate_sum(1, 2)
sum2 = calculate_sum(5, 5)
sum3 = calculate_sum(-1, 0)

print(sum1)
print(sum2)
print(sum3)

"""
2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar.
"""
def is_even(number):
    if number % 2 == 0:
        return True
    return False


print(is_even(2))
print(is_even(5))
"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""
def get_chars_number(nume, prenume, nume_mijlociu):
    total_chars = len(nume) + len(prenume) + len(nume_mijlociu)
    return total_chars


print(get_chars_number('Cosmina', 'Larisa', 'Bacter'))
print(get_chars_number('Ana', 'Maria', 'Pop'))
"""
4. Funcție care returnează aria dreptunghiului.
"""
def get_rectangle_area(width, height):
    return width * height


print(get_rectangle_area(1, 2))
print(get_rectangle_area(5, 2))
"""
5. Funcție care returnează aria cercului.
"""

def get_circle_area(r):
    import math

    return math.pi * r ** 2


area1 = get_circle_area(2)
area2 = get_circle_area(4)

print(area1)
print(area2)

"""
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
"""


def is_in_string(char, sequence):
    if char in sequence:
        return True
    return False


print(is_in_string('a', 'abc'))
print(is_in_string('b', 'def'))
"""
7. Funcție fără return, primește un string și printează pe ecran:
Numărul de caractere lower case este x.
Numărul de caractere upper case exte y.
"""

"""
8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.
"""
def print_lower_and_upper_chars(sequence):
    chars = {
        'lower': 0,
        'upper': 0
    }
    for char in sequence:
        if char.islower():
            chars['lower'] += 1
        elif char.isupper():
            chars['upper'] += 1

    print(f"Number of lowercase letters: {chars['lower']}")
    print(f"Number of uppercase letters: {chars['upper']}")


print_lower_and_upper_chars('aabbCCDD')
print_lower_and_upper_chars('aaa')
print_lower_and_upper_chars('ABCD')
print_lower_and_upper_chars('123')
"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ:
Primul număr x este mai mare decat al doilea număr y.
Al doilea număr y este mai mare decat primul număr x.
Numerele sunt egale.
"""

def compare_numbers(x, y):
    if x > y:
        print(f"Primul numar x {x} este mai mare decat al doilea y {y}.")
    elif x < y:
        print(f"Al doilea numar y {y} este mai mare decat primul numar x {x}")
    else:
        print("Numerele sunt egale")


compare_numbers(1, 2)
compare_numbers(4, 2)
compare_numbers(1, 1)
"""
10. Funcție care primește un număr și un set de numere.
Printează ‘am adaugat numărul nou în set’ + returnează True
Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
"""
def add_number_to_set(number, numbers_set):
    if number not in numbers_set:
        numbers_set.add(number)
        print('Am adaugat numarul nou in set')
        return True
    print('Nu am adaugat numarul nou in set. Acesta exista deja.')
    return False

"""
11. Funcție care primește o lună din an și returnează câte zile are acea lună.
"""

from calendar import monthrange

def luna_anului(luna):
    rezultat = monthrange(2023, luna)
    print(rezultat)
    return rezultat[1]

def count_days(month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        return 28  # 29 daca este an bisect
    return 0


print(count_days(1))
print(count_days(4))
print(count_days(2))

def count_days2(month):
    if month in ('ianuarie', 'martie', 'mai', 'iulie', 'august', 'octombrie', 'decembrie'):
        return 31
    elif month in ('aprilie','iunie', 'septembrie', 'noiembrie'):
        return 30
    elif month == 'februarie':
        return 28  # 29 daca este an bisect
    return 0

print(count_days2('ianuarie'))
print(count_days2('iunie'))
"""
12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.

În final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
"""
def calculator(a, b):
    suma = a + b
    diff = a - b
    multiplication = a * b

    if b != 0:
        division = a / b
    else:
        division = 0
    return suma, diff, multiplication, division


print(calculator(10, 2))
"""
13. Funcție care primește o listă de cifre (adică doar 0-9).
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""
def count_appearences(numbers):
    result = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }

    for key in result.keys():
        result[key] = numbers.count(key)

    return result


print(count_appearences([1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 6, 7, 9, 9, 9, 9, 9]))
print(count_appearences([1, 3, 1, 5, 9, 7, 7, 5, 5]))
"""
14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
"""

def get_max(a, b, c):
    numbers = [a, b, c]
    return max(numbers)


print(get_max(1, 2, 3))
print(get_max(5, 200, -300))
"""
15. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)
"""

def get_sum(a):
    result = 0
    for i in range(0, a + 1):
        result += i

    return result


print(get_sum(3))
print(get_sum(2))
print(get_sum(5))
"""
16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""

def get_common_values(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)


print(get_common_values([1, 2, 3, 3], [2, 3, 2, 4, 5]))


"""
17. Funcție care să aplice o reducere de preț.
Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.
"""

def apply_discount(price, discount):
    if 0 < discount <= 100:
        return price - price * discount / 100
    else:
        return 0


print(apply_discount(100, 10))
print(apply_discount(100, 120))
"""
18.Funcție care să afișeze data și ora curentă din România.
(bonus: afișează și data și ora curentă din China)
"""
import pytz
import datetime


def get_current_datetime(timezone):
    tz = pytz.timezone(timezone)
    current_datetime = datetime.datetime.now(tz)
    print(current_datetime)


# print(pytz.all_timezones)
get_current_datetime('Europe/Bucharest')
get_current_datetime('Asia/Shanghai')
"""
19. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta :)
"""

def countdown(day, month, year):
    import datetime

    data_curenta = datetime.date.today()
    data_dorita = datetime.date(year, month, day)
    if year < data_curenta.year:
        data_dorita = datetime.date(data_curenta.year, month, day)
    zile_ramase = (data_dorita - data_curenta).days
    print(f'Mai sunt {zile_ramase} zile pana la eveniment!')


countdown(25, 12, 2023)
countdown(29, 6, 1996)
