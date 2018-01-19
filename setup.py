#encoding:utf-8
from setuptools import setup, find_packages
import sys, os

version = '1.4.1'

setup(name='qiniu4blog',
      version=version,
      description="写博客用的七牛图床",
      long_description="""写博客用的七牛图床""",
      classifiers=[],
      keywords='python3 qiniu auto_upload',
      author='hackeryard',
      author_email='hrunker@gmail.com',
      url='https://github.com/hackeryard/qiniu4blog',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'qiniu',
		'pyperclip',
		'watchdog',
      ],
      entry_points={
        'console_scripts':[
            'qiniu4blog = qiniu4blog.qiniu4blog:main'
        ]
      },
)
