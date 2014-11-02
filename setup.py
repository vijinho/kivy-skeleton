import os

try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    from distutils.core import setup

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    version='1.0',
    name='skeleton',
    description='Skeleton',
    long_description='Skeleton is a skeleton application.',
    platforms = ['Linux','OSX','Android'],
    author='Vijay Mahrra',
    license='GPL3.0',
    classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Environment :: Desktop Environment',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License V3.0',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: Google :: Android',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Communications :: Personal'
          ],
    url='https://github.com/vijinho/skeleton',
    download_url='https://github.com/vijinho/skeleton',
    package_dir = {'.': ''},
    install_requires=[
        'nose>=1.3.4',
        'Click>=3.3',
        'Peewee>=2.3.3',
        'docutils'
    ],
    scripts=[],
    entry_points='''
        [console_scripts]
        skeleton=cli
    '''
)
