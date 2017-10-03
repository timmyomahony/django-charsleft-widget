import os
from setuptools import setup, find_packages

from charsleft_widget import VERSION

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='django-charsleft-widget',
    version=".".join(map(str, VERSION)),
    license='BSD License',
    description='A django widget that displays a normal text input with a remaining character count beside it.',
    long_description=readme,
    author="Timmy O'Mahony",
    author_email='hey@timmyomahony.com',
    url='https://github.com/timmyomahony/django-charsleft-widget',
    packages=find_packages(),
    package_data={
        'charsleft_widget': [
        ],
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',        
    ],        
)
