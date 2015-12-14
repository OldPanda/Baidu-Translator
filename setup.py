# encoding:utf-8
from setuptools import setup, find_packages
import sys
import os

version = "0.2"

setup(name="baidu",
      version=version,
      description="A English-Chinese translator running in terminal",
      long_description="A English-Chinese translator running in terminal",
      classifiers=[],
      keywords="python baidu translate",
      author="OldPanda",
      author_email="zjh0930@gmail.com",
      url="https://github.com/OldPanda/Baidu-Translator",
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
