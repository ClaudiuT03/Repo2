"""
PARTEA 1 - STRUCTURI DE DATE

Exerciții - studiu în workshopul de weekend
"""


"""
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o.
Inversează ordinea folosind slicing și suprascrie această listă.
Printează varianta actuală (inversată).
Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.

Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face suprascrierea automat și permanentizează aceste modificări. Ambele variante își găsesc utilitatea în funcție de ce ne dorim în acel moment. 
"""
list1 = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
# print(f"\n{list1}")
# list2 = list1[::-1]
# print(f"\n{list2}")
# list2.reverse()
# print(f"\nLista reinversată: , {list2}")
"""
2. De câte ori apare ‘do’?
"""
# lst = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(lst.count("do"))
"""
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
   Găsește 2 variante să le unești într-o singură listă. 
# """
# l1 = [3, 1, 0, 2]
# l2 = [6, 5, 4]
# l3 = l1+l2
# print(l3)
# l1.extend(l2)
# print(l1)
"""
4.
Sortează și afișează lista generată la exercițiul anterior.
"""
# l1 = [3, 1, 0, 2]
# l2 = [6, 5, 4]
# l3 = l1+l2
# l3.sort()
# print(l3)

"""
5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
Lista este goală.
Lista nu este goală.
"""
# if len(list3) == 0:
# # if list3 == []:
#     print("\nLista este goală.")
# else:
#     print("\nLista nu este goală.")

"""
6. Folosește o funcție care să șteargă lista de la exercițiul 3.
"""
# list3.clear()
"""
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
"""
# if list3:
#     print("\nLista nu este goală.")
# else:
#     print("\nLista este goală.")
"""
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
"""
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(dict1.keys())
"""
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
"""
# print(f"\nAna a luat nota {dict1['Ana']}")
# print(f"\nGigel a luat nota {dict1['Gigel']}")
# print(f"\nDorel a luat nota {dict1['Dorel']}")
# print(f"\nMaria a luat nota {dict1.get('Maria',-1)}")

"""
10. Dorel a făcut contestație și a primit 6
Modifică nota lui Dorel în 6
Printează nota după modificare
"""
# dict1['Dorel'] = 6
# print(dict1)

"""
11. Gigel se transferă din clasă
Căuta o funcție care să îl șteargă
Vine un coleg nou. Adaugă Ionică, cu nota 9
Printează noii elevi
"""
# del dict1['Gigel']
# dict1.update({'Ionica': 10})
# print(dict1)
"""
12. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

Declară o Listă cu 5 jucători
Schimbari_efectuate = te joci tu cu valori diferite
Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
Efectuează schimbarea 
Șterge jucătorul scos din listă
Adaugă jucătorul intrat
Afișază a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
Afișază ‘mai ai z schimbări’

Testează codul cu diferite valori

Google search hint
“how to check if item is în list python”
"""
# player_list = ['Rolando', 'Messi', 'Ibrahimovic', 'Benzema', 'Neymar']
# print(f"\nEchipa de jucători este formată din {player_list}")
# schimbari_efectuate = 3
# schimbari_max = 3
# y = str(input("Ce jucător înlocuiești: "))
# x = str(input("Ce jucător adaugi: "))
# if schimbari_efectuate < schimbari_max:
#      if y in player_list:
#         schimbari_efectuate += 1
#         player_list.remove(y)
#         player_list.append(x)
#         z = schimbari_max - schimbari_efectuate
#         print(f"\nA intrat {x}, a ieșit {y}, mai ai {z} schimbări")
#      else:
#         print(f"\nNu se poate efectua schimbarea deoarece jucătorul {y} nu e în teren")
# else:
#     print(f"\nNu mai sunt schimbări disponibile")
"""
13.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
Adaugă în zilele_sapt ‘luni’
Afișează zile_sapt
"""
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
# zile_sapt.add('luni')
# print(zile_sapt)
"""
14.Folosește un if și verifică dacă:
Weekend este un subset al zilelor din săptămânii.
Weekend nu este un subset al zilelor din săptămânii.
"""
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# if weekend.issubset(zile_sapt):
#     print("este subset")
# else:
#     print("nu este")
"""
15. Afișează diferențele dintre aceste 2 seturi.
"""
print(zile_sapt.difference(weekend))
print(weekend.difference(zile_sapt))
"""
16. Afișează intersecția elementelor din aceste 2 seturi.
"""
print(zile_sapt.intersection(weekend))