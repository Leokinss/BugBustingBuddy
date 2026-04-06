from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# BasePage provides common methods for all pages, such as finding elements, clicking, and sending keys.
class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            by, value = locator
            raise TimeoutException(
                f"❌ [{self.__class__.__name__}] Element not found in {timeout}s: {by} = '{value}'"
            )

    def send_keys(self, locator, text, timeout=10):
        try:
            element = self.find(locator, timeout)
            element.clear()  # optional: clear before typing
            element.send_keys(text)
        except TimeoutException:
            by, value = locator
            raise TimeoutException(
                f"❌ [{self.__class__.__name__}] Unable to send keys to element in {timeout}s: {by} = '{value}'"
            )

    def click(self, locator, timeout=10):
        """Wait for element to be clickable and click it."""
        try:
            element = self.find(locator, timeout)
            element.click()
        except TimeoutException:
            by, value = locator
            raise TimeoutException(
                f"❌ [{self.__class__.__name__}] Unable to click element in {timeout}s: {by} = '{value}'"
            )