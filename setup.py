#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Keshev Kulkarni",
    author_email="localized.analytics@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="AI utility functions for webscraping and selenium automation scripts",
    install_requires=[],
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"selenium_ai": ["py.typed"]},
    include_package_data=True,
    keywords="selenium_ai",
    name="selenium_ai",
    package_dir={"": "src"},
    packages=find_packages(include=["src/selenium_ai", "src/selenium_ai.*", "src/element_finder.*"]),
    setup_requires=['selenium', 'bs4'],
    url="https://github.com/KeshevK/SeleniumAI",
    version="0.1.0",
    zip_safe=False,
)
