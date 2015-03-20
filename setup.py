#!/usr/bin/env python
from setuptools import setup

setup( name='webplotlib',
       version='0.5',
       description='Expose matplotlib figures over http',
       author='Huy Nguyen',
       author_email='huy@huyng.com',
       packages=['webplotlib'],
       install_requires=["Flask"]
   )
       
# to distribute run:
# python setup.py register sdist bdist_wininst upload

