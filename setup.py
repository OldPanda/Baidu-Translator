# encoding:utf-8
from setuptools import setup, find_packages
import sys, os

version = "0.1"

setup(name="baidu", 
      version=version, 
      description="百度翻译查单词", 
      long_description="百度翻译查单词", 
      classifiers=[], 
      keywords="python baidu translate", 
      author="OldPanda", 
      author_email="zjh0930@gmail.com", 
      url="", 
      license="", 
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      entry_points={
        'console_scripts': [
            'baidu=baidu.baidu:main'
        ]
      }, 
      )