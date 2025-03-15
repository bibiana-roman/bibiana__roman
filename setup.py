
from setuptools import setup, find_packages

setup(
    name = "poo",
    version = "0.0.1",
    packages = find_packages(),
    author = "Bibiana Roman",
    author_email = "bibiana.roman@est.iudigital.edu.co",
    description = "",
    py_modules = ["actividad_1"],
    install_requires = [
        "pandas",
        "requests",
        "matplotlib",
        "openpyxl",
        "numpy"
    ]
)
