from setuptools import setup, find_packages

setup(
    name         = 'xmodem',
    version      = '0.2.4',
    author       = 'Wijnand Modderman',
    author_email = 'maze@pyth0n.org',
    description  = ('XMODEM protocol implementation.'),
    long_description = open('README.rst').read(),
    license      = 'MIT',
    keywords     = 'xmodem protocol',
    packages     = ['xmodem'],
    package_data = {'': ['doc/*.TXT']},
)

