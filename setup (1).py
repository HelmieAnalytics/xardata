from setuptools import find_packages, setup

setup(
    name='zaquity',
    packages=find_packages(include=['zaquity']),
    version='0.1.0',
    description='My first Python library',
    author='Helmie Research',
    install_requires=['yfinance','yahooquery==2.3.7'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)