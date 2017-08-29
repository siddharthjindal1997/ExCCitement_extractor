#!/usr/bin/env python

from setuptools import setup

setup(
    name='ExCCitement_extractor',
    version='0.1.0',
    author='Siddharth Jindal',
    author_email='siddharthjindal1997@gmail.com',
    packages=['ExCCitement_extractor'],
    scripts=[],
    url='https://github.com/siddharthjindal1997/exCCitement-extractor',
    license='LICENSE.txt',
    description='Python based sports video highlights extraction tool ',
    long_description=open('README.md').read(),
    install_requires=[
        "pyqt >4.0.0 ",
        "matplotlib>=2.0.0",
        "moviepy >=0.2",

    ],
    
)