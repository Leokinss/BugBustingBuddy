from pages.mobile.base_page import BasePage
from pages.mobile.catalog_page import CatalogPage
from pages.mobile.login_page import LoginPage
from pages.mobile.my_cart_page import MyCartPage
from pages.mobile.navigation_page import NavigationPage

# Container for all page objects to simplify access in tests
class Pages:
    def __init__(self, driver):
        self.base = BasePage(driver)
        self.navigation = NavigationPage(driver)
        self.login = LoginPage(driver)
        self.catalog = CatalogPage(driver)
        self.myCart = MyCartPage(driver)