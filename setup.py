# -*- coding: utf-8 -*-


from setuptools import setup


setup(
    name='csvshuf',
    packages=['csvshuf'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    entry_points={
        'console_scripts': ['csvshuf = csvshuf.csvshuf:main']
    },
    license='GNU GPLv3',
    url='https://github.com/pereorga/csvshuf',
    version='1.0.1',
    description='Shuffle cells by column in CSV files.',
    long_description=open('README.rst').read(),
    author='Pere Orga',
    author_email='pere@orga.cat',
    data_files=[('', ['LICENSE.md'])]
)
