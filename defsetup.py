from __future__ import division # confidence high

import distutils.core
import distutils.sysconfig
import distutils
import sys, os.path

try:
    import numpy
except:
    raise ImportError("NUMPY was not found. It may not be installed or it may not be on your PYTHONPATH")

pkg = [ "stsci.imagemanip", 'stsci.imagemanip.tests' ]

setupargs = {
      'version' :		"1.0",

      'description' :	"General Image Manipulation Tools",

      'author' :		"Christopher Hanley",

      'author_email' :	"help@stsci.edu",

      'license' :		"http://www.stsci.edu/resources/software_hardware/pyraf/LICENSE",

      'platforms' :		["Linux","Solaris","Mac OS X", "Windows"],

      'data_files' :	[('stsci/imagemanip',['LICENSE.txt'])],

      'package_dir' :   { 'stsci.imagemanip':'lib/stsci/imagemanip', 'stsci.imagemanip.tests':'lib/stsci/imagemanip/tests' },

      'ext_modules' :   [
                        distutils.core.Extension('stsci.imagemanip.bilinearinterp',['src/bilinearinterp.c'],
                             include_dirs = [ distutils.sysconfig.get_python_inc(), numpy.get_include() ] )
                        ]
}