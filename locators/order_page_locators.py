from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO_OPTION = (By.XPATH, '//button[normalize-space(.)="{}"]')
    PHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')

    DELIVERY_DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    SELECTED_DAY = (By.CSS_SELECTOR, '.react-datepicker__day--selected')
    RENTAL_PERIOD = (By.CLASS_NAME, 'Dropdown-control')
    RENTAL_OPTION = (By.XPATH, '//div[@class="Dropdown-option" and text()="{}"]')
    COLOR = (By.ID, '{}')
    COMMENT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '(//button[text()="Заказать"])[2]')
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Да"]')
    SUCCESS_HEADER = (
        By.XPATH,
        '//div[contains(@class, "Order_ModalHeader") and contains(., "Заказ оформлен")]',
    )
