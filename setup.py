# -*- coding: utf8 -*-
from setuptools import setup, find_packages

setup(
    name="OHappening",
    version="0.1.1",
    python_requires='>3.0.0',
    author="Ilmo Salmenperä",
    author_email="ilmo.salmenpera@helsinki.fi",
    packages=find_packages(),
    include_package_data=True,
    url="http://github.com/MrCubanfrog/OHappening",
    license="LICENSE",
    description="PyQt5 application for showing multiple google calendars in a single calendar",
    install_requires=[
        "PyQt5",
    ],
    long_description=open("README.md").read(),
    entry_points='''
        [console_scripts] 
        ohappen=ohappening.ohappening:start
    ''',
)
