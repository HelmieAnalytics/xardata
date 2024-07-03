from setuptools import find_packages, setup

setup(
    name='zaquitydata',
    
    packages=find_packages(include=['zaquitydata']),
    
    version='0.1.5',
    
    description='A stock price data import package',
    
    author='HelmieAnalytics',

    url='https://github.com/HelmieAnalytics/zaquitydata',
    
    long_description= open('README.md').read(),#+ '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type = "text/markdown",

    install_requires= ['yfinance','yahooquery<=2.3.7','requests>=2.31.0'],

    setup_requires= ['pytest-runner'],

    tests_require= ['pytest==4.4.1'],

    test_suite= 'tests',

    keywords= ['Data Mining', 'Data Science', 'Equities', 'Stocks'],
)
