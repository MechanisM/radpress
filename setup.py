#!/usr/bin/env python
import os.path
from distutils.core import setup
from radpress import get_version

setup(
    name='radpress',
    version=get_version(),
    description='Simple reusable blog application',
    author='Gokmen Gorgen',
    author_email='gokmen@radity.com',
    url='',
    packages=['radpress'],
    scripts=[os.path.join('scripts', 'radpress')]
)
