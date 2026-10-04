from selenium.webdriver.common.by import By


class BaseLocators:
    """Общие элементы главной страницы и страницы заказа."""

    YANDEX_LOGO = (By.CSS_SELECTOR, 'a[class*="Header_LogoYandex"]')
    SCOOTER_LOGO = (By.CSS_SELECTOR, 'a[class*="Header_LogoScooter"]')
    TOP_ORDER_BUTTON = (By.XPATH, '(//button[text()="Заказать"])[1]')
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")
