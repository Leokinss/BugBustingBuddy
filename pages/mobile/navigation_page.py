from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from pages.mobile.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class NavigationPage(BasePage):
    APP_LOGO_AND_NAME = (AppiumBy.ACCESSIBILITY_ID, "App logo and name")
    NAV_BUTTON_MENU = (AppiumBy.ACCESSIBILITY_ID, "View menu")
    NAV_LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Login Menu Item")
    NAV_LOGOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Logout Menu Item")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_menu(self):
        self.click(self.NAV_BUTTON_MENU)

    def go_to_login_page(self):
        self.open_menu()
        self.click(self.NAV_LOGIN_BUTTON)
    
    def is_logout_button_visible(self):
        return self.is_element_visible(self.NAV_LOGOUT_BUTTON)
    
    def is_app_logo_and_name_visible(self):
        return self.is_element_visible(self.APP_LOGO_AND_NAME, timeout=10)