from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.base_locators import BaseLocators


class BasePage:
    """Общие ожидания, действия и элементы страниц."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        def try_click(driver):
            try:
                driver.find_element(*locator).click()
                return True
            except (
                ElementClickInterceptedException,
                ElementNotInteractableException,
            ):
                return False

        self.wait.until(try_click)

    def click_scooter_logo(self):
        self.click_element(BaseLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(BaseLocators.YANDEX_LOGO)

    def click_top_order_button(self):
        self.click_element(BaseLocators.TOP_ORDER_BUTTON)

    def accept_cookies(self):
        self.click_element(BaseLocators.COOKIE_ACCEPT_BUTTON)

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    def fill_field(self, locator, value):
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(value)

    def switch_to_new_window(self, old_handles):
        self.wait.until(EC.new_window_is_opened(old_handles))
        new_handle = next(
            handle for handle in self.driver.window_handles if handle not in old_handles
        )
        self.driver.switch_to.window(new_handle)

    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))
        return self.driver.current_url
