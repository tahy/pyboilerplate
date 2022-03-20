#!/usr/bin/env python
import os
from setuptools import setup, find_packages
from os.path import join, dirname

lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = lib_folder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

setup(name='PACK_NAME',
      version='0.1',
      description='PACK_NAME description',
      author='Pavel Potapov',
      author_email='tahy.gm@gmail.com',
      url='https://github.com/tahy/PACK_NAME',
      packages=find_packages(),
      long_description=open(join(dirname(__file__), 'README.md')).read(),
      entry_points={
          'console_scripts':
              ['PACK_NAME-start = PACK_NAME.main:run', ]
      },
      install_requires=install_requires,
      )
