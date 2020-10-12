# -*- coding: utf-8 -*-
"""
The setup script for the fplib module. 
"""

#%% Modules
import os
from setuptools import setup

#%% Reading of readme
cwd = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(cwd, 'README.rst')) as h:
  long_description = h.read()

#%% Actual setup
setup(
  name="fplib",
  version='0.1.1',
  description="A functional programming library for python.",  
  long_description=long_description, 
  long_description_content_type='text/x-rst', 
  author="Miroslav Hruska",
  author_email="hruska.miro@gmail.com", 
  url='https://github.com/hruskamiro/fplib', 
  py_modules=['fplib'], 
  license="MIT", 
  keywords="functional programming",
  )
