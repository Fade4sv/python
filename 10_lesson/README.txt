### Запуск всех тестов проекта:

pytest --alluredir=allure-results


### Запуск конкретного файла с тестами:
 **Для калькулятора:**

  pytest test_calcs.py --alluredir=allure-results

 **Для магазина:**

  pytest test_shop.py --alluredir=allure-results




## Просмотр сформированного отчета

После завершения тестов в корне проекта появится папка `allure-results`.


allure generate allure-results -o allure-report

-o allure-report`** — указывает имя папки, куда сохранится готовый сайт отчета.

Для открытия сгенерированного отчета из папки используйте команду:

allure open allure-report