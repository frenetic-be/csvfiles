#!/usr/bin/env python
import csvfiles

from distutils.core import setup

setup(name='csvfiles',
      version=csvfiles.__version__,
      description='Simple module to read .csv files and transfer the content into a dictionary',
      long_description='''
      Simple module to read .csv files and transfer the content into a dictionary
      ''',
      author='Julien Spronck',
      author_email='frenticb@hotmail.com',
      url='http://frenticb.com/',
      packages=['csvfiles'],
      license='Free for non-commercial use',
     )