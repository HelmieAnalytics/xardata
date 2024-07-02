from setuptools import find_packages, setup

setup(
    name='Zaquitydata',
    packages=find_packages(include=['Zaquitydata']),
    version='0.1.0',
    description='A stock price data import package',
    author='Helmie Analytics',
    install_requires=['yfinance','yahooquery==2.3.7'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
