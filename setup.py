import os
from setuptools import setup, find_packages

from charsleft_widget import VERSION


setup(
    name='django-charsleft-widget',
    version=".".join(map(str, VERSION)),
    license='BSD License',
    author="Timmy O'Mahony",
    author_email='hey@timmyomahony.com',
    description='A django widget that displays a normal text input with a remaining character count beside it.',
    long_description=open('README.md').read(),
    url='https://github.com/timmyomahony/django-charsleft-widget',
    packages=find_packages(),
    package_data={
        'charsleft_widget': [
        ],
    },
    include_package_data=True,
    # _Should_ work back to 1.10 but untested
    install_requires=[
        "Django >= 1.8",
    ],
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
