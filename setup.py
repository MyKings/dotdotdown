#!/usr/bin/env python
# coding: utf-8

from setuptools import find_packages, setup

from dotdotdown import __author__
from dotdotdown import __version__

setup(
    name='dotdotdown',
    version=__version__,
    author=__author__,
    author_email='xsseroot@gmail.com',
    license='LICENSE',
    keywords="dotdotdown, The Directory Traversal Downloader",
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "dotdotdown = dotdotdown.cli:main"
        ]
    },
    install_requires=[
        'requests',
        'requests[socks]',
        'lxml'
    ],
    packages=find_packages()
)
