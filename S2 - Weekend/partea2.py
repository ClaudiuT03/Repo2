"""

PARTEA 2: CICLURI REPETITIVE

Exerciții - studiu în workshopul de weekend

"""

"""
1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel'] 

Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# #v0
# for i in range(0,len(masini)):
#     print(f"\nMașina mea preferată este {masini[i]}")
# #
# # # v1 - v2 prescurtat
# # [print(f"\nMașina mea preferată este {m}") for m in masini]
# #
# #v2
# for m in masini:
#     print(f"\nMașina mea preferată este {m}")
# #
# #v3
# m = 0
# while m < len(masini):
#     print(f"\nMașina mea preferată este {masini[m]}")
#     m += 1
"""
2. Aceeași listă:
Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in range(0,len(masini)):
#     if i == 0 or i == len(masini)-1:
#         continue
#     masini[i] = masini[i].upper()
#
# else:
#     print(masini)
"""
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in range(0,len(masini)):
#     if masini[i] == 'Mercedes':
#         print("Am gasit masina dorita de dumneavoastra")
#         break
#     print(f'Am gasit masina {masini[i]}. Mai cautam')
#
# for i in masini:
#     if i == 'Mercedes':
#         print("Am gasit masina dorita de dumneavoastra")
#         break
#     print(f'Am gasit masina {i}. Mai cautam')


"""
4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 

Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# # for each
# for masina in masini:
#     if masina == "Trabant" or masina == "Lăstun":
#         continue
#     print(f"S-ar putea sa va placa masina {masina}")

"""
5. Modernizează parcul de mașini:

Crează o listă goală, masini_vechi.
Iterează prin mașini.
Când găsesti Lăstun sau Trabant:
Salvează aceste mașini în masini_vechi.
Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
Printează Modele vechi: x.
Modele noi: x.
"""
# masini_vechi = []
# for masina in masini:
#     if masina == 'Lăstun' or masina == 'Trabant':
#         masini_vechi.append(masina)
#         masini.remove(masina)
#         masini.append('Tesla')
#
#
# print(masini_vechi)
# print(masini)
"""
6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.

Prezintă doar mașinile care se încadrează în acest buget.
Iterează prin dict.items() și accesează mașina și prețul.
Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
Iterează prin listă.
"""
# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# for masina, pret in pret_masini.items():
#     if pret <= 15000:
#         print(f"Pentru un buget de sub 15000 euro puteți alege mașină {masina}")

"""
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea.
Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# trei = 0
# for nr in numere:
#     if nr == 3:
#         trei += 1
# print(trei)
"""
8. Aceeași listă:
Iterează prin ea
Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""
# suma = 0
# for nr in numere:
#   suma += nr
# print(suma)
"""
9. Aceeași listă:
Iterează prin ea.
Afișază cel mai mare număr (nu ai voie să folosești max).
"""
# maxim = numere[0]
# for nr in numere:
#     if nr > maxim:
#         maxim = nr
# print(maxim)
"""
10. Aceeași listă:
Iterează prin ea.
Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
Afișază noua listă.
"""
# for index in range(0,len(numere)):
#     if numere[index] > 0:
#         numere[index] *= -1
# print(numere)
"""
11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere 
Populează corect celelalte liste
Afișează cele 4 liste la final
"""
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for nr in alte_numere:
#     if nr % 2 == 0 and nr > 0:
#         numere_pare.append(nr)
#     elif nr % 2 != 0 and nr > 0:
#         numere_impare.append(nr)
#     if nr > 0:
#         numere_pozitive.append(nr)
#     else:
#         numere_negative.append(nr)
# print(numere_pare)
# print(numere_impare)
# print(numere_pozitive)
# print(numere_negative)
"""
12. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
"""
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# a = alte_numere[0]
# alta_lista = []
# for nr in alte_numere:
#     if nr < a:
#         alta_lista.append(nr)
#         a +=1
# print(alta_lista)
"""
13. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
   User alege un număr
   Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!
"""

"""
14. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
"""

"""
15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
"""

"""
Exerciții Recomandate - studiu individual                                        .

1. Revizualizează sesiunile din această săptămână și ia notițe în caz că ți-a scăpat ceva.

2. Vizualizează din cursul  ‘Primii pași în Programare’ de la sectiunile de mai jos:
Structuri de date 
Flow Control
"""
