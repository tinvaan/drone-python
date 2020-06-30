#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


def requirements():
    with open('./requirements.txt', 'r') as f:
        return f.read().splitlines()


setup(
    name='PyDrone',
    version='1.0.0',
    py_modules=['drone'],
    include_package_data=True,
    install_requirements=requirements()
)

