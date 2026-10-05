"""Два набора данных: верхняя и нижняя кнопки заказа соответственно."""

ORDER_CASES = [
    {
        "entry_point": "top",
        "delivery_in_days": 1,
        "first_name": "Анна",
        "last_name": "Иванова",
        "address": "Москва, улица Лесная, дом 10",
        "metro": "Сокольники",
        "phone": "79001234567",
        "rental_period": "сутки",
        "color": "black",
        "comment": "Позвонить перед доставкой",
    },
    {
        "entry_point": "bottom",
        "delivery_in_days": 2,
        "first_name": "Иван",
        "last_name": "Петров",
        "address": "Москва, улица Тверская, дом 15",
        "metro": "Черкизовская",
        "phone": "79007654321",
        "rental_period": "двое суток",
        "color": "grey",
        "comment": "Оставить у подъезда",
    },
]
