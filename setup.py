from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='react.py',
  version='0.0.1',
  description='Alternative to Flask to create your own HTML Components',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  url='',  
  author='DS_Stift007',
  author_email='dsstift@icloud.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='dscjobs discord', 
  packages=find_packages(),
  install_requires=['flask','loguru'] 
)
