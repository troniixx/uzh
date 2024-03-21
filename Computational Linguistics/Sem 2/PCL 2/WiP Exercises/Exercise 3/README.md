# PCL 2 Exercise 3

## Introduction
Welcome to Exercise 3 of PCL 2! In this exercise, you will learn how to transform a Python module `readability_analysis.py` into an open-source package that can be published and shared with others. The main objectives include:

1. Understanding the purpose and creation of a pyproject.toml file.
2. Structuring the code into an object-oriented package.
3. Uploading the package to TestPyPI.

First let's familiarize ourselves with `readability_analysis.py`. This module aims to calculate and interpret the readability of a given text using two popular readability tests: the Flesch-Kincaid and Gunning Fog indices. These tests analyze statistical factors like average sentence length, word length, and word difficulty to assess text complexity.

## Feedback
If you want to get feedback from us, you can submit your code through Gitlab before **March 19th at 23:59**. Submissions after this deadline will not receive feedback.
* Please start by forking this project, which will create a personal copy of the exercise repository. 
* Add your name and matriculation number to every file you submit. 


## Task 1: Write a `pyproject.toml` file
The pyproject.toml file is crucial for defining build configurations and dependencies in Python projects. It provides a standardized way to manage project settings and dependencies. Your first task is to create a `pyproject.toml` file in the root directory of the project. Below is a template to help you:

```
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my_project"
version = "0.0.1"
authors = [
    { name="Anonymous", email="anonymous@example.com" }
]
description = "A project to calculate and interpret the readability of a given text"
readme = "README.md"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
requires-python = ">=3.9"
dependencies = []

[tool.hatch.build.targets.wheel]
packages = ["src/readability_analysis"]

```


To specify which version of spaCy and Pyphen you need in dependencies, follow these steps:

1. Go to the PyPI website (https://pypi.org/). 
2. Use the search bar to find the package name and its latest version number.
3. Consider using the `~=`, `<=`, or `<` operators to allow compatibility with the latest version of the packages.

Note: Do not include the spaCy module `en_core_web_sm` in dependencies, as it is [not hosted on PyPI](https://github.com/explosion/spaCy/issues/3536#issuecomment-633231083). Including it will cause errors when uploading to TestPyPI later. Instead, manually install it using the command `python -m spacy download en_core_web_sm`.


## Task2: Prepare the code for publishing
Now, let's package our project! We'll convert the single Python file readability_analysis.py into an object-oriented package. You can refer to the provided test file, `test_readability_analysis.py`, for ideas on how to start with the restructuring process. However, feel free to adjust the test files according to your preferences. Below is a suggested package structure, but you're welcome to customize it as needed:

```
my_project/
├── src/
│   └── readability_analysis/
│       ├── __init__.py
│       ├── __main__.py
│       ├── analyzer.py
│       └── indices.py
├── tests/
│   ├── test_analyzer.py
│   └── test_indices.py
├── pyproject.toml
└── README.md
```

Note: You're not required to write a README.md file for this project, but you're encouraged to do so!


## Task 3: Implement CI/CD testing pipeline
Having completed the previous exercises, you should be familiar with the "autograding" pipeline. Now, your task is to add a `gitlab-ci.yml` file based on the provided unit tests and then implement the testing pipeline on Gitlab. You can use one of the `gitlab-ci.yml` files from previous exercises as template for guidance.


## Task 4: Upload the package to TestPyPI
Finally, try to upload the package to [TestPyPI](https://test.pypi.org/), a testing environment for Python packages. Follow these basic steps:

1. Install `build` and `twine` if not already installed: `pip install build twine`
2. Create a distribution package: `python -m build`
3. Upload the package to TestPyPI: `twine upload --repository testpypi dist/*`
4. If required, you can set up API tokens in your TestPyPI `Account settings`.
5. In case you encounter any errors during the upload process, you can use the following command to get more detailed information: `twine upload --repository testpypi dist/* --verbose`

For more detailed guidance on using TestPyPI, refer to [Using TestPyPI](https://packaging.python.org/en/latest/guides/using-testpypi/) if you are not familiar with TestPyPI.
