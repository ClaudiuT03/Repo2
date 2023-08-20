

"""
1. Intrati pe site-ul https://www.elefant.ro/
"""
import time
import unittest
from selenium import webdriver


class TestElefantPage(unittest.TestCase):
    LINK = "https://www.elefant.ro/"

    def setUp(self):
        # cream driverul
        self.driver = webdriver.Chrome()
        # accesam link-ul www.elefant.ro

        self.driver.get(self.LINK)
        # maximizam fereastra de browser
        self.driver.maximize_window()
        time.sleep(2)

    def tearDown(self):
        # inchidem browserul
        self.driver.quit()

    def test_x(self):
        pass

"""
2. Cautati un produs la alegere (iphone 14) si verificati ca s-au returnat
cel putin 10 rezultate ([class="product-title"])
"""


"""
3. Extrageti din lista produsul cu pretul cel mai mic [class="current-price "]
din primele 10 produse gasite
(puteti sa va folositi de find_elements)
"""


"""
4. Extrageti titlul paginii si verificati ca este corect
"""


"""
5. Intrati pe site, accesati butonul cont si click pe conectare.
Identificati elementele de tip user si parola si inserati valori incorecte
(valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid)
- Dati click pe butonul "conectare" si verificati urmatoarele:
             1. Faptul ca nu s-a facut logarea in cont
            2. Faptul ca se returneaza eroarea corecta
"""


"""
6. Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@")
si verificati faptul ca butonul "conectare" este dezactivat
"""
