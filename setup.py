#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import holonet

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = holonet.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-holonet',
    version=version,
    description="""This package is used to control holonet from a django project.""",
    long_description=readme + '\n\n' + history,
    author='Abakus Webkom',
    author_email='webkom@abakus.no',
    url='https://github.com/webkom/django-holonet',
    packages=[
        'holonet',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-holonet',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
