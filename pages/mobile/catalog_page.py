from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from pages.mobile.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class CatalogPage(BasePage):
    CATALOG_PAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, "title")
    ADD_TO_CART_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Tap to add product to cart")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_catalog_page_title_visible(self)-> bool:
        try:
            self.find(self.CATALOG_PAGE_TITLE, timeout=5)
            return True
        except TimeoutException:
            return False

    def get_product_by_name(self, product_name: str) -> tuple[AppiumBy, str]:
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{product_name}")'
        )

    def add_to_cart(self, product_name: str) -> None:
        locator = self.get_product_by_name(product_name)
        
        # move 50 pixels above the element and click because only the image can be clicked
        self.click_offset(locator, y_offset=-50)
        
        # click the "Add to Cart" button as usual
        self.click(self.ADD_TO_CART_BUTTON)