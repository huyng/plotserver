#!/usr/bin/env python
from setuptools import setup

with open('README.rst', 'r') as f:
    readme = f.read()

setup( name='webplot',
       version='0.6',
       description='Expose matplotlib figures over http',
       long_description=readme,
       author='Huy Nguyen',
       author_email='huy@huyng.com',
       packages=['webplot'],
       install_requires=["Flask"],
       url="https://github.com/huyng/webplot"
   )
       
# to distribute run:
# python setup.py register sdist  upload

