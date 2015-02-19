#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '0.0.2'

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

version = __version__

readme = open('README.rst').read()

setup(
    name='django-holonet',
    version=version,
    description="""This package is used to control holonet from a django project.""",
    long_description=readme,
    author='Abakus Webkom',
    author_email='webkom@abakus.no',
    url='https://github.com/webkom/django-holonet',
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    install_requires=[
    ],
    license="MIT",
    zip_safe=False,
    keywords='django-holonet',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
