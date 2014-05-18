#!/usr/bin/env python
import os
import sys

import bit9

from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with open('README.md') as f:
    readme = f.read()
with open('HISTORY.rst') as f:
    history = f.read()

setup(name='bit9-api'
        ,version=bit9.__version__
        ,description='Bit9 API for their Cyber Forensics Service'
        ,long_description=readme + '\n\n' + history
        ,url='https://github.com/blacktop/bit9-api'
        ,author='blacktop'
        ,author_email='dev@blacktop.io'
        ,license=bit9.__license__
        ,test_suite="tests"
        ,packages=['bit9']
        ,package_dir={'requests': 'requests'}
        ,install_requires=["requests >= 2.2.1"])
