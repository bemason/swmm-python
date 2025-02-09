# -*- coding: utf-8 -*-

#
#  __init__.py - SWMM toolkit package
#
#  Created:    Aug 9, 2018
#  Updated:    May 19, 2021
#
#  Author:     See AUTHORS
#

'''
A low level pythonic API for the swmm-output and swmm-solver dlls using SWIG.
'''


__author__ = "See AUTHORS"
__copyright__ = "None"
__credits__ = "Colleen Barr, Sam Hatchett"
__license__ = "CC0 1.0 Universal"

__version__ = "0.9.0"
__date__ = "June 7, 2021"

__maintainer__ = "Michael Tryby"
__email__ = "tryby.michael@epa.gov"
__status__  = "Beta"


import os
import platform
import sys


# Adds directory containing swmm libraries to path
if platform.system() == "Windows":
    libdir = os.path.join(os.path.dirname(__file__), "../../swmm_toolkit")

    if hasattr(os, 'add_dll_directory'):
       if 'conda' in sys.version:
           os.environ['CONDA_DLL_SEARCH_MODIFICATION_ENABLE']="1"
       os.add_dll_directory(libdir)
    else:
        os.environ["PATH"] = libdir + ";" + os.environ["PATH"]
