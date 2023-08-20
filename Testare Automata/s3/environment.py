from browser import Browser
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def before_all(context):
    """
    Vom defini toate instructiunile care trebuie
    executate sau pe care vrem sa le facem disponibile inaintea
    TUTUROR testelor/pasilor
    """
    context.browser = Browser()
    context.login_page_object = LoginPage()
    context.inventory_page_object = InventoryPage()


def after_all(context):
    """
    Vom defini toate instructiunile care trebuie executate
    sau pe care vrem sa le facem disponibile DUPA TOATE testele
    """
    context.browser.close()