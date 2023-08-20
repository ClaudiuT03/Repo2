import time
import unittest

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager


class TestElefantPage(unittest.TestCase):
    LINK = "https://www.elefant.ro/"
    SEARCH_BOX = (By.CLASS_NAME, "js-has-overlay")
    SEARCH_BUTTON = (By.CLASS_NAME, "btn-search")
    COOKIE = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    SEARCH_RESULT = (By.CLASS_NAME, "search-result-headline")
    CURRENT_PRICE = (By.CLASS_NAME, "current-price ")
    BUTTON_CONECTARE = (By.CLASS_NAME, "logged-out-dot")
    # BUTTON_CONECTARE = (By.CLASS_NAME, "logged-out-dot")

    def setUp(self):
        # cream driverul
        self.driver = webdriver.Chrome()

        # acesam linkul www.elefant.ro
        self.driver.get(self.LINK)

        # maximizam fereastra browser
        self.driver.maximize_window()
        time.sleep(2)

        # acceptam cookies
        cookie_cancel = self.driver.find_element(*self.COOKIE)
        cookie_cancel.click()

    def tearDown(self):
        # inchidem browserul
        self.driver.quit()

    def test_homepage(self):
        """
        4. Extrageti titlul paginii si verificati ca este corect
        """
        homepage = self.driver.title
        expected_title = "elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • Peste 500.000 de produse pentru tine!"
        self.assertEqual(homepage, expected_title, "Titlul nu corespunde cu cel din browser")

    def test_search_iphone14_list_items(self):
        """
        2. Cautati un produs la alegere (iphone 14) si verificati ca s-au returnat
        cel putin 10 rezultate ([class="product-title"])
        """
        search = self.driver.find_element(*self.SEARCH_BOX)
        search.click()
        search.send_keys("iphone 14")

        search_enter = self.driver.find_element(*self.SEARCH_BUTTON)
        search_enter.click()
        time.sleep(3)

        iphone14_items = self.driver.find_elements(By.CSS_SELECTOR, '[class="product-title"]')
        print(len(iphone14_items))
        self.assertGreaterEqual(len(iphone14_items), 10)

    def test_search_iphone14_result_text(self):
        search = self.driver.find_element(*self.SEARCH_BOX)
        search.click()
        search.send_keys("iphone 14")

        search_enter = self.driver.find_element(*self.SEARCH_BUTTON)
        search_enter.click()
        time.sleep(3)
        result_headline = self.driver.find_element(*self.SEARCH_RESULT)
        result_text = result_headline.text
        result_list = result_text.split()
        print(result_list)
        total_items = result_list[-2]
        self.assertGreaterEqual(int(total_items),10)

        """
        3. Extrageti din lista produsul cu pretul cel mai mic [class="current-price "]
        din primele 10 produse gasite
        (puteti sa va folositi de find_elements)
        """

    def test_produs_pret_mic(self):
        search = self.driver.find_element(self.SEARCH_BOX)
        search.click()
        search.send_keys("iphone 14")
        search_enter = self.driver.find_element(self.SEARCH_BUTTON)
        search_enter.click()
        time.sleep(3)
        total_current_prices = self.driver.find_elements(*self.CURRENT_PRICE)
        current_prices = total_current_prices[:10]
        print(len(current_prices))
        prices = []
        for price in current_prices:
            price_info = price.text
            price_info_list = price_info.split()
            price_value = price_info_list[0].replace(".", "").replace(",", ".")
            print(price_value)
            price_value_float = float(price_value)
            prices.append(price_value_float)
        min_price = min(prices)
        self.assertGreater(min_price, 10)


"""
5. Intrati pe site, accesati butonul cont si click pe conectare.
Identificati elementele de tip user si parola si inserati valori incorecte
(valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid)
- Dati click pe butonul "conectare" si verificati urmatoarele:
             1. Faptul ca nu s-a facut logarea in cont
            2. Faptul ca se returneaza eroarea corecta
"""


def test_invalid_account(self):
    self.driver.find_element(*self.ACCOUNT_BUTTON).click()
    time.sleep(1)
    self.driver.find_element(*self.CONNECT_BUTTON).click()
    email = self.driver.find_element(*self.EMAIL_BUTTON)
    password = self.driver.find_element(*self.PASSWORD_BUTTON)
    email.click()
    email.send_keys("flaviu@gmail.abc")
    password.click()
    password.send_keys("flaviu")
    time.sleep(1)
    self.driver.find_element(*self.CONECTARE_BUTTON).click()
    current_error = self.driver.find_element(By.XPATH, "//*[@class='alert alert-danger']").text
    expected_error = "Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou."
    current_url = self.driver.current_url
    expected_url = "https://www.elefant.ro/INTERSHOP/web/WFS/elefant-elefantRO-Site/ro_RO/-/RON/ViewUserAccount-ProcessLogin"
    self.assertEqual(current_error, expected_error, "Eroarea afisata nu este acceasi cu cea asteptata!")
    self.assertEqual(current_url, expected_url, "Url-urile nu coincid")


"""
6. Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@")
si verificati faptul ca butonul "conectare" este dezactivat
"""


# def test_invalid_email(self):
#
#     self.newsletter_cancel()
#     self.driver.find_element(*self.ACCOUNT_BUTTON).click()
#     time.sleep(1)
#     self.driver.find_element(*self.CONNECT_BUTTON).click()
#     email = self.driver.find_element(*self.EMAIL_BUTTON)
#     time.sleep(1)
#     email.send_keys("flaviu")
#     conectare = self.driver.find_element(*self.CONECTARE_BUTTON)
#     actual = conectare.get_property("disabled")
#     expected = True
#     self.assertEqual(actual, expected)
#
#
# def newsletter_cancel(self):
#     newletter_x_button = (By.CLASS_NAME, "close")
#     newletter_box = (By.CSS_SELECTOR, '[class ="weblayer--bar-subscription"]')
#     ## class="weblayer--bar-subscription vertical-center horizontal-center enter-slide-up"
#     try:
#         self.driver.find_element(*newletter_x_button).click()
#     except selenium.common.exceptions.NoSuchElementException:
#         pass
#
