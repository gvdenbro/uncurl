#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='uncurl2yaml',
    version='0.0.3',
    description='A library to convert curl requests to yaml.',
    author='Gregory Vandenbroucke',
    author_email='gvdenbro@gmail',
    url='https://github.com/gvdenbro/uncurl',
    entry_points={
        'console_scripts': [
            'uncurl2yaml = uncurl2yaml.bin:main',
        ],
    },
    install_requires=['xerox', 'six'],
    packages=find_packages(exclude=("tests", "tests.*")),
)
