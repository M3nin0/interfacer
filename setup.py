#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from setuptools import find_packages, setup

readme = open('README.md').read()

install_requires = [
    'pandas',
    'numpy',
    'rpy2',
]

packages = find_packages()

g = {}
with open(os.path.join('interfacer', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='interfacer',
    version=version,
    packages=packages,
    author="Felipe Carlos",
    author_email="felipe.carlos@inpe.br",
    include_package_data=True,
    description="Pacote para facilitar a utilização do descdist em Python",
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=install_requires,
)
