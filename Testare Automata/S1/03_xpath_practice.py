import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
time.sleep(1)

# accesam un link
LINK = 'https://carturesti.ro/'
driver.get(LINK)
time.sleep(2)

# maximizam fereastra
driver.maximize_window()
time.sleep(2)


"""
1. XPATH - Gaseste butonul "COMANDA-L AICI", incepand de la elementul div cu clasa homePage

Verifica ca tag-ul acestuia este a.
Da click pe buton si verifica ca link-ul curent este cel asteptat.
"""

"""
2. XPATH - Gaseste elementul cu textul 'Împachetare gratuită'

Verifica ca tag-ul acestuia este h4.
"""

"""
3. XPATH - cauta elementul div care se afla imediat dupa
elementul de tip i cu clasa 'cartu-icons-giftbox'
"""

"""
4. XPATH - cauta elementul h4 care se afla exact ianintea elementului
span cu textul 'peste 120.000 de produse! '
"""
