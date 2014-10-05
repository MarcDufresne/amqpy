#!/usr/bin/env python3

import sys
import os
import subprocess

from setuptools import setup, find_packages

import amqpy

name = 'amqpy'
description = 'an AMQP 0.9.1 client library for Python >= 3.2.0'

if sys.version_info < (3, 2):
    raise Exception('amqpy requires Python 3.2 or higher')

classifiers = [
    'Development Status :: 4 - Beta',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
    'Intended Audience :: Developers',
]

package_data = {
    '': ['*.md', '*.ini', 'AUTHORS', 'LICENSE'],
}

keywords = ['amqp', 'rabbitmq', 'qpid']


def long_description():
    if os.path.exists('README.md') and os.system('which pandoc > /dev/null') == 0:
        args = ['pandoc', '-f', 'markdown', '-t', 'rst', 'README.md']
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.DEVNULL)
        out, _ = p.communicate()
        p.wait(1)
        return out.decode('UTF-8')
    else:
        return description


setup(
    name=name,
    description=description,
    long_description=long_description(),
    version=amqpy.__version__,
    author=amqpy.__author__,
    author_email=amqpy.__contact__,
    maintainer=amqpy.__maintainer__,
    url=amqpy.__homepage__,
    platforms=['any'],
    license='LGPL',
    packages=find_packages(exclude=['ez_setup', 'tests', 'tests.*']),
    package_data=package_data,
    tests_require=['pytest>=2.6'],
    classifiers=classifiers,
    keywords=keywords
)
