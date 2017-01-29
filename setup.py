import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_adm_apiutils',
    version='0.1.4',
    packages=find_packages(),
    include_package_data=True,
    license='GPL 3',  # example license
    description='Some django abstract model',
    long_description=README,
    url='https://github.com/ADMAutomation/Django-ADM-APIUtils',
    author='Alfredo Di Maria',
    author_email='linuxloverstaff@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',  # keep updated "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL 3',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
