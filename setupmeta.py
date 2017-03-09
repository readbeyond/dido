#!/usr/bin/env python
# coding=utf-8

# dido is an API server and Web application for the aeneas forced aligner
#
# Copyright (C) 2017, Alberto Pettarin (www.albertopettarin.it)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Metadata for setting the dido package up
"""

import io

__author__ = "Alberto Pettarin"
__email__ = "dido@readbeyond.it"
__copyright__ = "Copyright 2017, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "GNU AGPL v3"
__status__ = "Production"
__version__ = "0.0.1"

##############################################################################
#
# you might need to edit the information below this line
#
##############################################################################

# package version
# NOTE: generate a new one for each PyPI upload, otherwise it will fail
PKG_VERSION = "0.0.1.0"

# required packages to install
# NOTE: always use exact version numbers
# NOTE: this list should be the same as requirements.txt
PKG_INSTALL_REQUIRES = [
    "aeneas>=1.7.2",
    "boto3>=1.4.2",
    "requests>=2.9.1",
    "tgt>=1.4.2",
    "youtube-dl>=2016.9.27",
]

# required packages to install extra tools
PKG_EXTRAS_REQUIRE = {}

# packages to be distributed
# NOTE: not including the dido.test package to keep the size small
PKG_PACKAGES = [
    "dido",
]

# data files to be distributed
# NOTE: .py files will be added automatically
PKG_PACKAGE_DATA = {
    "dido": [
        "res/*",
        "*.md"
    ],
}

# scripts to be installed globally
# on Linux and Mac OS X, use the file without extension
# on Windows, use the file with .py extension
PKG_SCRIPTS = []

##############################################################################
#
# do not edit the metadata below this line
#
##############################################################################

# package name
PKG_NAME = "dido"

# package author
PKG_AUTHOR = "Alberto Pettarin"

# package author email
PKG_AUTHOR_EMAIL = "alberto@albertopettarin.it"

# package URL
PKG_URL = "https://github.com/readbeyond/dido"

# package license
PKG_LICENSE = "GNU Affero General Public License v3 (AGPL v3)"

# human-readable descriptions
PKG_SHORT_DESCRIPTION = "dido is an API server and Web application for the aeneas forced aligner"
try:
    PKG_LONG_DESCRIPTION = io.open("README.rst", "r", encoding="utf-8").read()
except:
    PKG_LONG_DESCRIPTION = PKG_SHORT_DESCRIPTION

# PyPI keywords
PKG_KEYWORDS = [
    "aeneas",
    "dido",
]

# PyPI classifiers
PKG_CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Affero General Public License v3",
    "Natural Language :: English",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Topic :: Education",
    "Topic :: Multimedia",
    "Topic :: Multimedia :: Sound/Audio",
    "Topic :: Multimedia :: Sound/Audio :: Analysis",
    "Topic :: Multimedia :: Sound/Audio :: Speech",
    "Topic :: Printing",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Text Processing",
    "Topic :: Text Processing :: Linguistic",
    "Topic :: Text Processing :: Markup",
    "Topic :: Text Processing :: Markup :: HTML",
    "Topic :: Text Processing :: Markup :: XML",
    "Topic :: Utilities"
]
