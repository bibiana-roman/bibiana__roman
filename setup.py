
from setuptools import setup, find_packages

setup(
    name = "poo",
    version = "0.0.1",
    packages = find_packages(),
    author = "Bibiana Roman",
    author_email = "bibiana.roman@est.iudigital.edu.co",
    description = "",
    py_modules = ["actividades"],
    install_requires = [
        "kagglehub[pandas-datasets]>=0.3.8",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.2",
        "pandas",
        "numpy",
        "openpyxl",
        "requests"
    ]
)
