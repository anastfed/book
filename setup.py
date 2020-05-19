# -*- coding: utf-8 -*-
from setuptools import setup

import sys

# (sys).setdefaultencoding("UTF-8")

setup(
    name='robokassa',
    version='1.3',
    author='Anastasia Fedulova',
    author_email='',

    packages=['robokassa', 'robokassa.migrations'],

    url='http://chitalocka.ru/',
    license='MIT license',
    description=u'Читалочка'.encode('utf8'),
    long_description=open('README.rst').read().encode('utf8') + u"\n\n" + open('CHANGES.rst').read().encode('utf8'),

    requires=['django (>= 1.3)'],

    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7.0'
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)