from datetime import date, timedelta

import allure
import pytest

from data.order_data import ORDER_CASES
from data.urls import BASE_URL
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:
    @allure.title("Успешный заказ самоката")
    @pytest.mark.parametrize("order_data", ORDER_CASES, ids=["top_button", "bottom_button"])
    def test_create_order(self, driver, order_data):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()
        main_page.start_order(order_data["entry_point"])

        delivery_date = (
            date.today() + timedelta(days=order_data["delivery_in_days"])
        ).strftime("%d.%m.%Y")

        order_page = OrderPage(driver)
        order_page.fill_customer_info(order_data)
        order_page.fill_rental_info(order_data, delivery_date)
        order_page.submit_order()

        assert "Заказ оформлен" in order_page.get_success_message()
