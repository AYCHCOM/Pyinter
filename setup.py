from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pyinter',
      version=version,
      description="An interval package which deals with open, closed or half open intervals.",
      long_description="""\
Another Python package with deals with interval arithmetic, this one hopes to be useful.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='interval range discontinous-range union intersection',
      author='Inti Ocean',
      author_email='',
      url='intiocean.com',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )