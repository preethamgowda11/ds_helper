from setuptools import setup, find_packages
setup(
    name="ds_helper",
    version="0.1.0",
    description="A library with tools for column type detection, data visualization, and text cleaning.",
    author="Preetham Gowda",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
        "wordcloud",
        "nltk"
    ],
    python_requires=">=3.7",
)