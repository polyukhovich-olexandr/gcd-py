### Greatest Common Denominator on Python 🐍 with tests

НСД на Python

В файлі **gcd.py** є функція **gcd()**, яка сприймає **2** значення, і повертає їх найбільший спільний дільник

Також можна запустити тестування:

### Тестування pytest

Встановіть **pytest** у ваше середовище Python:

    pip install pytest

або

    python -m pip install pytest

Щоб запустити тест з файлу **test_gcd.py**, виконавши команду:

    pytest test_gcd.py -q

або

    python -m pytest test_gcd.py -q

Якщо буде написано **passed**, то всі тести пройшли успішно

Також можете написати свої pytest-тести, назвіть функцію з початком на **test_** , і при запуску pytest-теста вона буде враховуватися

### Тестування Hypothesis


Встановіть **Hypothesis** у ваше середовище Python:

    pip install pytest hypothesis --upgrade

або

    python -m pip install pytest hypothesis --upgrade

Щоб запустити тест з файлу **gcd.py**, виконавши команду:

    pytest gcd.py -q

або

    python -m pytest gcd.py -q

Якщо буде написано **passed**, то всі тести пройшли успішно