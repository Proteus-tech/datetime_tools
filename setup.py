#!/usr/bin/env python

from distutils.core import setup

setup(name='datetime_tools',
      version='1.4',
      description='Datetime tools for Django',
      author='Proteus Technologies',
      author_email='team@proteus-tech.com',
      url='http://proteus-tech.com',
      packages=['datetime_tools', 'datetime_tools.templatetags'],
     )