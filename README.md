# selenium-ai
<p align="center">

<a href="https://pypi.python.org/pypi/selenium_ai">
<img src="https://img.shields.io/pypi/v/selenium_ai.svg" /></a>
<a href="https://travis-ci.org/KeshevK/selenium_ai"><img src="https://travis-ci.org/KeshevK/selenium_ai.svg?branch=master" /></a>
</p>
AI utility functions for webscraping and selenium automation scripts

## Installation

    pip install selenium-ai

## Requirements

* Written for Python 3.3+
* Requires selenium, bs4
* Requires installation of geckodriver compatible with selenium. Read about setup [here](https://selenium-python.readthedocs.io/installation.html)

<sub><sup>[back to top](#selenium-ai)</sub></sup>

## Features

The following features are available:

* [find_elements_by_attribute_pattern](#find_elements_by_attribute_pattern): returns elements with attributes that match a regex pattern.

### Find Elements by Attribute Pattern

    from selenium_ai import ElementFinder

    from selenium import webdriver
    driver = webdriver.Firefox()
    element_finder = ElementFinder(driver)

    driver.get("https://bing.com")
    elements = element_finder.find_elements_by_attribute_pattern("enter your search term")

Returns list of selenium elements

<sub><sup>[back to top](#find_elements_by_attribute_pattern)</sub></sup>

# Credits
This package was created with Cookiecutter and the `cs01/cookiecutter-pypackage` project template.

[Cookiecutter](https://github.com/audreyr/cookiecutter)

[cs01/cookiecutter-pypackage](https://github.com/cs01/cookiecutter-pypackage)
