"""
Installs ecks using setuputils

Run:

  python setup.py install

to install this package using this script. 

To install the latest public release use run:

  pip install ecks
"""


try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup, find_packages


import sys


required_python_version = '3.5'


if sys.version < required_python_version:
    print("Ecks3 requires python %s or later, you have %s" % (required_python_version, sys.version))
    sys.exit(1)


setup(
    name="Ecks3",
    version="0.11-dev",
    description="Easy access to SNMP data",
    long_description="A simple way to get data out of a remote machine using SNMP without having to deal with a single MIB or OID.",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Monitoring"
    ],
    author="Chris Read",
    author_email="chris.read@gmail.com",
    url="https://github.com/alexanderfefelov/ecks3",
    license="Apache 2.0",
    packages=find_packages(),
    keywords="snmp monitoring",
    install_requires="pysnmp >= 4.2.2"
)
