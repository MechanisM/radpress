# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

pkg_name = 'radpress'
version = __import__(pkg_name).__version__

setup(
    name=pkg_name,
    version=version,
    description='Simple reusable blog application',
    author=u'Gökmen Görgen',
    author_email='gokmen@radity.com',
    license='GPLv3',
    url='https://github.com/radity/radpress',
    packages=find_packages(exclude=['venv', 'demo', 'docs']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>=1.4',
        'docutils>=0.9',
        'Pygments>=1.5',
        'PIL>=1.1.7',
        'easy-thumbnails>=1.0.3'
    ]
)
