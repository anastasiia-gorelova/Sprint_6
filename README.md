# Sprint_6

UI-автотесты учебного сервиса [«Яндекс.Самокат»](https://qa-scooter.education-services.ru/).
Проект реализован на Python с Selenium, pytest и Allure, с использованием Page Object Model.
Тесты выполняются в Mozilla Firefox.

## Покрытие

Всего 12 независимых тестовых случаев:

| Файл | Случаев | Проверки |
| --- | ---: | --- |
| `test/test_faq.py` | 8 | Раскрытие каждого вопроса, видимость соответствующего ответа и точное совпадение его текста с ожидаемым |
| `test/test_order.py` | 2 | Полный позитивный сценарий заказа с двумя наборами данных: через верхнюю и нижнюю кнопки «Заказать», заполнение обоих шагов, подтверждение и появление окна «Заказ оформлен» |
| `test/test_navigation.py` | 2 | Переход со страницы заказа на главную Самоката по логотипу; открытие новой вкладки по логотипу Яндекса и переход на `https://ya.ru/` |

FAQ и заказы параметризованы. Каждая точка входа в заказ проверяется один раз,
со своим набором данных. Даты доставки вычисляются относительно дня запуска:
завтра и послезавтра. Логотипы проверяются отдельными тестами со страницы заказа.

## Структура проекта

```text
Sprint_6/
├── data/
│   ├── faq_data.py                 # Ожидаемые ответы FAQ
│   ├── order_data.py               # Два набора данных заказа
│   └── urls.py                     # Адреса страниц
├── locators/
│   ├── base_locators.py            # Общие элементы страниц
│   ├── main_page_locators.py       # FAQ и нижняя кнопка заказа
│   └── order_page_locators.py      # Форма и модальные окна заказа
├── pages/
│   ├── base_page.py                # Ожидания, клики, ввод, прокрутка, окна
│   ├── main_page.py                # Действия на главной странице
│   └── order_page.py               # Заполнение и подтверждение заказа
├── test/
│   ├── test_faq.py
│   ├── test_order.py
│   └── test_navigation.py
├── allure_results/                # Результаты запусков для Allure
├── allure-report/                 # Сгенерированный HTML-отчёт
├── conftest.py                     # Фикстура Firefox
├── pytest.ini                     # Параметры pytest и путь результатов
├── requirements.txt               # Зависимости Python
├── .gitignore
└── README.md
```

В пакетах присутствуют файлы `__init__.py`. Методы взаимодействия с браузером
находятся в `pages/`, локаторы — в `locators/`, проверки — в `test/`.
Общие элементы и действия вынесены в классы `BaseLocators` и `BasePage`.

## Установка зависимостей

Нужны Python 3.10 или новее, установленный Mozilla Firefox и доступ к интернету.
Команды для macOS/Linux выполняются из корня проекта:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Selenium Manager подбирает geckodriver при запуске. При первом запуске может
понадобиться его скачивание. Каждый тест получает отдельный Firefox с видимым
окном и размером по умолчанию; после теста браузер закрывается.

## Запуск тестов

Полный набор с очисткой результатов предыдущих запусков Allure:

```bash
python -m pytest --clean-alluredir
```

Отдельные группы:

```bash
python -m pytest test/test_faq.py
python -m pytest test/test_order.py
python -m pytest test/test_navigation.py
```

Проверка сбора тестов без запуска браузера:

```bash
python -m pytest --collect-only
```

Для сокращённого вывода ошибок можно добавить `--tb=short`.

## Allure

Названия, функциональные группы и шаги тестов оформлены через Allure.
Путь `allure_results/` задан в `pytest.ini`, поэтому результаты сохраняются
автоматически при запуске pytest.

Для просмотра нужен отдельно установленный Allure CLI. Пакет `allure-pytest`
является интеграцией с pytest и не устанавливает команду `allure`.

Просмотр отчёта:

```bash
allure serve allure_results
```

Сохранение HTML-отчёта:

```bash
allure generate allure_results --clean -o allure-report
allure open allure-report
```

Окружение и кеши исключены из Git. Результаты последнего полного запуска
в `allure_results/` и HTML-отчёт в `allure-report/` включены в проект.
