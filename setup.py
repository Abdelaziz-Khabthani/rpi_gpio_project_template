""" setup.py definition file """

from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setup(
    name='rpi_gpio_project_template',
    version='0.0.1',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Abdelaziz Khabthani',
    author_email='abdelaziz.khabthani@gmail.com',
    entry_points={
        'console_scripts': ['rpi_gpio_project_template=rpi_gpio_project_template.rpi_gpio_project_template:main']
    },
    packages=find_packages(
        include=['rpi_gpio_project_template', 'rpi_gpio_project_template.*']
    ),
    install_requires=[
        'colorzero==1.1',
        'gpiozero==1.5.1',
        'RPi.GPIO==0.7.0',
    ]
)
