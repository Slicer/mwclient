#!/usr/bin/env python
# encoding=utf-8
from __future__ import print_function
import os
import sys

try:
    from setuptools import setup
    from setuptools.command.test import test as TestCommand
except ImportError:
    print("This package requires 'setuptools' to be installed.")
    sys.exit(1)


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'mwclient/README.txt')).read()

setup(name='mwclient',
      version='0.6.5',  # Rember to also update __ver__ in client.py
      description='MediaWiki API client',
      long_description=README,
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7'
      ],
      keywords='mediawiki wikipedia',
      author='Bryan Tong Minh',
      author_email='bryan.tongminh@gmail.com',
      url='https://github.com/mwclient/mwclient',
      license='MIT',
      packages=['mwclient']
      )
