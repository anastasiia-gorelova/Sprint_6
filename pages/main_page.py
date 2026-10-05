import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """Действия с главной страницей сервиса."""

    @allure.step("Открыть вопрос FAQ с индексом {question_index}")
    def open_faq_question(self, question_index):
        by, template = MainPageLocators.FAQ_QUESTION
        locator = (by, template.format(question_index))
        self.scroll_to_element(locator)
        self.click_element(locator)

    @allure.step("Получить видимый ответ FAQ с индексом {question_index}")
    def get_faq_answer_text(self, question_index):
        by, template = MainPageLocators.FAQ_ANSWER
        locator = (by, template.format(question_index))
        return self.find_visible_element(locator).text

    @allure.step("Начать заказ через кнопку: {entry_point}")
    def start_order(self, entry_point):
        if entry_point == "top":
            self.click_top_order_button()
        elif entry_point == "bottom":
            self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
            self.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        else:
            raise ValueError(f"Неизвестная точка входа: {entry_point}")
