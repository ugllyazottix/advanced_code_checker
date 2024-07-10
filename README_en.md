
# Advanced Code Checker

This plugin provides more thorough code checking for errors using static analysis tools such as `pylint`, `mypy` and `pycodestyle`.

## Installation

You can install the package using pip:

bash
pip install advanced_code_checker


## Usage

python
from advanced_code_checker import check_code

file_path = "your_script.py"
results = check_code(file_path)
print(results)