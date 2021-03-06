#!/usr/bin/env python
from shutil import rmtree
from setuptools import setup

setup(
    name="elasticmodels",
    version=__import__('elasticmodels').__version__,
    url='https://github.com/PSU-OIT-ARC/elasticmodels',
    author='Matt Johnson',
    author_email='mdj2@pdx.edu',
    description="",
    packages=['elasticmodels','elasticmodels.management', 'elasticmodels.management.commands'],
    zip_safe=False,
    install_requires=[
        'elasticutils',
        'six',
    ],
    classifiers=[
        'Framework :: Django',
    ],
)
