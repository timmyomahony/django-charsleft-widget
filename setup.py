import os
from setuptools import setup, find_packages

from charsleft_widget import VERSION

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='django-charsleft-widget',
    version=".".join(map(str, VERSION)),
    description='A django widget that displays a normal text input with a remaining character count beside it.',
    long_description=readme,
    author="Timmy O'Mahony",
    author_email='timmy@pastylegs.com',
    url='https://github.com/pastylegs/django-charsleft-widget',
    packages=find_packages(),
    package_data = {
        'charsleft_widget': [
        ],
    },
)