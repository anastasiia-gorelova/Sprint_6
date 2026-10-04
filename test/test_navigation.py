import allure

from data.urls import BASE_URL, ORDER_URL, YANDEX_URL
from pages.order_page import OrderPage


@allure.feature("Навигация по логотипам")
class TestNavigation:
    @allure.title("Логотип Самоката возвращает с заказа на главную страницу")
    def test_scooter_logo_opens_main_page(self, driver):
        page = OrderPage(driver)
        page.open(ORDER_URL)
        page.click_scooter_logo()

        assert page.wait_for_url(BASE_URL) == BASE_URL

    @allure.title("Логотип Яндекса открывает главную Яндекса в новом окне")
    def test_yandex_logo_opens_yandex_in_new_window(self, driver):
        page = OrderPage(driver)
        page.open(ORDER_URL)
        old_handles = driver.window_handles
        page.click_yandex_logo()
        page.switch_to_new_window(old_handles)

        assert len(driver.window_handles) == len(old_handles) + 1
        assert page.wait_for_url(YANDEX_URL) == YANDEX_URL
