from selenium.webdriver.common.by import By


class MainPageLocators:
    FAQ_QUESTION = (By.ID, "accordion__heading-{}")
    FAQ_ANSWER = (By.ID, "accordion__panel-{}")

    BOTTOM_ORDER_BUTTON = (By.XPATH, '(//button[text()="Заказать"])[2]')
