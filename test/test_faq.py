import allure
import pytest

from data.faq_data import FAQ_CASES
from data.urls import BASE_URL
from pages.main_page import MainPage


@allure.feature("Вопросы о важном")
class TestFaq:
    @allure.title("Вопрос FAQ №{question_index}: открывается соответствующий ответ")
    @pytest.mark.parametrize(
        "question_index, expected_answer",
        FAQ_CASES,
        ids=[
            "price_and_payment",
            "multiple_scooters",
            "rental_time",
            "same_day_order",
            "extend_or_return_early",
            "charger",
            "cancel_order",
            "outside_mkad",
        ],
    )
    def test_question_opens_matching_answer(self, driver, question_index, expected_answer):
        page = MainPage(driver)
        with allure.step("Открыть главную страницу и закрыть уведомление о cookies"):
            page.open(BASE_URL)
            page.accept_cookies()

        page.open_faq_question(question_index)
        actual_answer = page.get_faq_answer_text(question_index)

        with allure.step("Сравнить полный текст ответа с ожидаемым"):
            assert actual_answer == expected_answer, (
                f"Неверный ответ на вопрос с индексом {question_index}: "
                f"ожидали {expected_answer!r}, получили {actual_answer!r}"
            )
