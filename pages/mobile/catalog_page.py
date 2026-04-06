from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from pages.mobile.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class CatalogPage(BasePage):
    CATALOG_PAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, "title")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_catalog_page_title_visible(self):
        try:
            self.find(self.CATALOG_PAGE_TITLE, timeout=5)
            return True
        except TimeoutException:
            return False