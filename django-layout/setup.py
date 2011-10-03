# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

PACKAGE = os.environ['PACKAGE']
VERSION = os.environ['VERSION']

setup(name=PACKAGE, version=VERSION,
      packages=find_packages('src/python'), package_dir={'': 'src/python'})

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
