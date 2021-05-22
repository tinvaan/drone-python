#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import abspath, dirname, join
from setuptools import setup, find_packages


def requirements():
    with open('./requirements.txt', 'r') as f:
        return f.read().splitlines()


def description():
    basedir = dirname(abspath(__file__))
    with open(join(basedir, "README.md"), 'r') as f:
        return f.read()


setup(
    name='drone-python',
    version='1.0.0',
    description="Python client for the Drone CI public API",
    long_description=description(),
    long_description_content_type="text/markdown",
    url="https://github.com/tinvaan/pydroneio",
    author="Harish Navnit",
    author_email="harishnavnit@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements(),
    python_requires=">3.6"
)
