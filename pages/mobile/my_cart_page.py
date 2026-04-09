from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from pages.mobile.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class MyCartPage(BasePage):
    MY_CART_LOCATOR = (AppiumBy.ACCESSIBILITY_ID, "Displays number of items in your cart")

    def go_to_my_cart_page(self):
        self.click(self.MY_CART_LOCATOR)

    def get_product_locator(self, product_name: str) -> tuple[AppiumBy, str]:
        return (
            AppiumBy.XPATH,
            f"//*[@text='{product_name}']"
        )

    def is_product_in_cart(self, product_name: str) -> bool:
        locator = self.get_product_locator(product_name)
        return self.is_element_visible(locator)