from selenium.webdriver.common.by import By

from base_page import BasePage


class LoginPage(BasePage):
    LOGIN_URL = 'https://www.saucedemo.com/'
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login-button')
    ERROR_LOGIN = (By.XPATH, '//h3[@data-test="error"]')

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_URL)

    def insert_correct_username(self):
        username_element = self.driver.find_element(*self.USERNAME)
        username_element.send_keys('standard_user')

    def insert_correct_password(self):
        password_element = self.driver.find_element(*self.PASSWORD)
        password_element.send_keys('secret_sauce')

    def insert_incorrect_password(self):
        password_element = self.driver.find_element(*self.PASSWORD)
        password_element.send_keys('123')

    def insert_incorrect_username(self):
        username_element = self.driver.find_element(*self.USERNAME)
        username_element.send_keys('1234')

    def insert_locked_username(self):
        username_element = self.driver.find_element(*self.USERNAME)
        username_element.send_keys('locked_out_user')

    def click_login_btn(self):
        login_btn = self.driver.find_element(*self.LOGIN_BTN)
        login_btn.click()

    def check_error_message(self, expected_err_msg):
        err_element = self.driver.find_element(*self.ERROR_LOGIN)
        actual_err_msg = err_element.text
        assert expected_err_msg == actual_err_msg, "Error messages are different"