#!/usr/bin/env python
from setuptools import setup

with open('README.rst', 'r') as f:
    readme = f.read()

setup( name='plotserver',
       version='0.5',
       description='Expose matplotlib figures over http',
       long_description=readme,
       author='Huy Nguyen',
       author_email='huy@huyng.com',
       packages=['plotserver'],
       install_requires=["Flask"],
       url="https://github.com/huyng/plotserver"
   )

# to distribute run:
# python setup.py register sdist  upload
