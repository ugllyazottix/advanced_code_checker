# Advanced Code Checker

Этот плагин предоставляет более тщательную проверку кода на ошибки с использованием инструментов static analysis таких как `pylint`, `mypy` и `pycodestyle`.

## Установка

Вы можете установить пакет с помощью pip:

bash
pip install advanced_code_checker


## Использование

python
from advanced_code_checker import check_code

file_path = "your_script.py"
results = check_code(file_path)
print(results)
