#!/usr/bin/env python3
import otpy
from setuptools import setup

setup(
    version='0.10.0',
    url='https://github.com/cathalgarvey/otpy',
    license="GNU Affero General Public License v3",
    name='otpy',
    description='One-time password systems (time or counter) in Python 3',
    long_description=otpy.__doc__,
    author='Cathal Garvey',
    author_email='cathalgarvey@cathalgarvey.me',
    packages=['otpy'],
    platforms="any",
    classifiers = [
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3"
    ]
)
