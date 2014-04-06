try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

setup(
    name='bit9_api',
    test_suite="tests",
    version='1',
    packages=['bit9', 'bit9.test'],
    url='https://github.com/blacktop/bit9-api',
    license='GPLv3',
    author='blacktop',
    author_email='',
    description='Bit9 API for their Cyber Forensics Service',
    install_requires=[
        "requests >= 2.2.1",
    ],
)
