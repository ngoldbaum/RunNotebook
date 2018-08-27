from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="RunNotebook",
    version="0.3.1",
    author="Nathan Goldbaum",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email="nathan12343@gmail.com",
    url="https://github.com/ngoldbaum/RunNotebook",
    packages=["RunNotebook"],
    install_requires=["sphinx", "jupyter", "nbconvert", "nbformat"]
)
