# -*- coding: utf-8 -*-
from os.path import join, dirname
from setuptools import setup, find_packages
import sys
import os

VERSION = (1, 0)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

f = open(join(dirname(__file__), 'README.rst'))
long_description = f.read().strip()
f.close()

install_requires = [
"smbus2",
]


setup(
    name = 'tsl2561-smbus2',
    description = "SMBus2 driver for the TSL2561 digital luminosity (light) sensors",
    license = "BSD",
    url = "https://github.com/frillip/tsl2561",
    download_url = "https://github.com/frillip/tsl2561",
    long_description = long_description,
    version = __versionstr__,
    author = "Phil Martin",
    author_email = "root@frillip.com",
    packages = find_packages(
        where='.',
    ),
    keywords = ['TSL2561', 'smbus2'],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    install_requires=install_requires,
)
