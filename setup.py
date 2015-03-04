#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pip.req import parse_requirements


README = open("README.md").read()
CHANGES = open("CHANGES").read()
PACKAGE_DESCRIPTION = "%s\n%s" % (README, CHANGES)
REQUIREMENTS = [str(r.req) for r in parse_requirements("requirements.txt")]

REQUIREMENTS.append("distribute")


setup(
    name="django-userapp",
    version=u":versiontools:django_userapp:",
    description="Django userapp integration",
    long_description=PACKAGE_DESCRIPTION,
    keywords="django, userapp, django-userapp",
    author="Sultan Imanhodjaev",
    author_email="sultan.imanhodjaev@gmail.com",
    maintainer="Sultan Imanhodjaev",
    maintainer_email="sultan.imanhodjaev@gmail.com",
    url="https://github.com/imanhodjaev/django-userapp",
    license="LGPL",
    include_package_data=True,
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    setup_requires=["versiontools >= 1.9.1"],
    package_data={"package": "tests/*"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP :: Session",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration :: Authentication/Directory"
    ]
)
