#!/usr/bin/env python
import recon.release
from glob import glob
from numpy import get_include as np_include
from setuptools import setup, find_packages, Extension


version = recon.release.get_info()
recon.release.write_template(version, 'stsci/imagemanip')

setup(
    name = 'stsci.imagemanip',
    version = version.pep386,
    author = 'Christopher Hanley',
    author_email = 'help@stsci.edu',
    description = 'STScI general image manipulation tools',
    url = 'https://github.com/spacetelescope/stsci.imagemanip',
    classifiers = [
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires = [
        'nose',
        'numpy',
        'sphinx',
        'stsci.sphinxext',
        'stsci.tools'
    ],
    packages = find_packages(),
    package_data = {
        '': ['LICENSE.txt'],
    },
    ext_modules=[
        Extension('stsci.imagemanip.bilinearinterp',
            ['src/bilinearinterp.c'],
            include_dirs=[np_include()],
            define_macros=[('NUMPY', '1')])
    ],
)
