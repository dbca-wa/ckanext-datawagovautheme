#!/usr/bin/env/python
from setuptools import setup

setup(
    name='ckanext-datawagovautheme',
    version='0.2.0',
    description='DBCA theme',
    license='AGPL3',
    author='Florian Mayer',
    author_email='florian.mayer@dbca.wa.gov.au',
    url='http://govhack2015.readthedocs.org/',
    namespace_packages=['ckanext'],
    packages=['ckanext.datawagovautheme'],
    zip_safe=False,
    entry_points = """
        [ckan.plugins]
        datawagovau_theme = ckanext.datawagovautheme.plugins:DBCATheme
    """
)
