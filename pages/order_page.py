import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    """Два шага формы заказа и подтверждение результата."""

    @allure.step("Заполнить данные получателя и перейти к аренде")
    def fill_customer_info(self, data):
        self.fill_field(OrderPageLocators.FIRST_NAME, data["first_name"])
        self.fill_field(OrderPageLocators.LAST_NAME, data["last_name"])
        self.fill_field(OrderPageLocators.ADDRESS, data["address"])
        self.fill_field(OrderPageLocators.METRO, data["metro"])
        by, template = OrderPageLocators.METRO_OPTION
        self.click_element((by, template.format(data["metro"])))
        self.fill_field(OrderPageLocators.PHONE, data["phone"])
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить параметры аренды, дата доставки: {delivery_date}")
    def fill_rental_info(self, data, delivery_date):
        self.fill_field(OrderPageLocators.DELIVERY_DATE, delivery_date)
        self.click_element(OrderPageLocators.SELECTED_DAY)
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        by, template = OrderPageLocators.RENTAL_OPTION
        self.click_element((by, template.format(data["rental_period"])))
        by, template = OrderPageLocators.COLOR
        self.click_element((by, template.format(data["color"])))
        self.fill_field(OrderPageLocators.COMMENT, data["comment"])

    @allure.step("Нажать «Заказать» и подтвердить заказ кнопкой «Да»")
    def submit_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Дождаться окна успешного заказа и получить его текст")
    def get_success_message(self):
        return self.find_visible_element(OrderPageLocators.SUCCESS_HEADER).text
