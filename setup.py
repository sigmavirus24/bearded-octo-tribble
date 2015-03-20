#!/usr/bin/env python

# Copyright 2015, Rackspace US, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools
import sys

from openvas import info

if sys.version_info < (2, 7, 0):
    sys.stderr.write("This requires Python 2.7.0 or greater \n")
    sys.exit('Upgrade python because your version of it is VERY deprecated\n')

with open('README.rst', 'rb') as r_file:
    README = r_file.read()

setuptools.setup(
    name=info.__appname__,
    version=info.__version__,
    author=info.__author__,
    author_email=info.__email__,
    description=info.__description__,
    long_description=README,
    license='Apache2',
    packages=['openvas',
              'openvas.openvas_reports'],
    package_data={'openvas': ['static/rackspace/img/*',
                              'static/rackspace/css/*',
                              'static/rackspace/scss/*',
                              'static/rackspace/js/*',
                              'templates/*.html',
                              'templates/openvas/*.html',
                              'templates/openvas/openvas/*']},
    url=info.__url__,
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content']
)
