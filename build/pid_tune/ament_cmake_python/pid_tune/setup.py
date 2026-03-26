from setuptools import find_packages
from setuptools import setup

setup(
    name='pid_tune',
    version='0.0.0',
    packages=find_packages(
        include=('pid_tune', 'pid_tune.*')),
)
