#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='PyDrone',
    version='1.0.0',
    py_modules=['drone'],
    include_package_data=True,
    install_requirements=[
        "requests==2.24.0"
    ]
)

