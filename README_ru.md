# Advanced Code Checker

���� ������ ������������� ����� ���������� �������� ���� �� ������ � �������������� ������������ static analysis ����� ��� `pylint`, `mypy` � `pycodestyle`.

## ���������

�� ������ ���������� ����� � ������� pip:

bash
pip install advanced_code_checker


## �������������

python
from advanced_code_checker import check_code

file_path = "your_script.py"
results = check_code(file_path)
print(results)
