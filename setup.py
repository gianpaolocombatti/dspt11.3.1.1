"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup


setup(
    name='dspt11_lambda_john_r',  # Required
    version='0.0.2',  # Required
    author='DSPT11',  # Optional
    author_email='john.renken@lambdaschool.com',  # Optional
    keywords='reddit',  # Optional
    packages=['mymodule'],  # Required
    python_requires='>=3.6, <4',
    install_requires=['pandas', 'psycopg2'],  # Optional
)