from base_page import BasePage


class InventoryPage(BasePage):

    def check_current_url(self):
        expected_url = 'https://www.saucedemo.com/inventory.html'
        actual_url = self.driver.current_url
        assert expected_url == actual_url, "Error: Invalid URL"
