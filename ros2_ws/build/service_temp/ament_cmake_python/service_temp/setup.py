from setuptools import find_packages
from setuptools import setup

setup(
    name='service_temp',
    version='0.0.0',
    packages=find_packages(
        include=('service_temp', 'service_temp.*')),
)
