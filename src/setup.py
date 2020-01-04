#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import setup

setup(
    name="pytest-gitcov",
    packages=["pytest-gitcov"],
    version="{tag}.dev{commitcount}+{gitsha}",

    # the following makes a plugin available to pytest
    entry_points={
        "pytest11": ["gitcov = pytest-gitcov.pluginmodule"],
    },

    # custom PyPI classifier for pytest plugins
    classifiers=["Framework :: Pytest"],
)
