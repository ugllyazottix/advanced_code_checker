# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="advanced_code_checker",
    version="0.1.0",
    author="uglyazotix",
    author_email="uglyazotix",
    description="Плагин для более тщательной проверки кода на ошибки",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ugllyazottix/advanced_code_checker",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pylint",
        "mypy",
        "pycodestyle",
    ],
)