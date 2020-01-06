#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io

from os.path import dirname
from os.path import join

from setuptools import setup
from setuptools import find_packages


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='pytest-gitcov',
    version_format='{tag}.{commitcount}',

    licence='MIT',
    author='David James McCorrie',
    author_email='djmccorrie@gmail.com',

    url='https://github.com/machshev/pytest-gitcov',
    description='Pytest plugin for reporting on coverage of the last git commit.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    setup_requires=[
        'setuptools-git-version',
    ],

    install_requires=[
        'pytest-cov',
        'coverage',
    ],

    tests_require=[
        'pyhamcrest',
        'unittest',
    ],

    entry_points={
        'pytest11': [
            'pytest_gitcov = pytest_gitcov.plugin',
        ]
    },

    scripts=[
        'bin/git-py-coverage'
    ],

    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
    ],
)
