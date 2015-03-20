#!/usr/bin/env python
from setuptools import setup

setup( name='webplot',
       version='0.5',
       description='Expose matplotlib figures over http',
       author='Huy Nguyen',
       author_email='huy@huyng.com',
       packages=['webplot'],
       install_requires=["Flask"],
       url="https://github.com/huyng/webplot"
   )
       
# to distribute run:
# python setup.py register sdist  upload

