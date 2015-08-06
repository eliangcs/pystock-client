try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import codecs
import os
import re
import sys


here = os.path.abspath(os.path.dirname(__file__))

py3 = sys.version_info[0] == 3


# Read the version number from a source file.
# Why read it, and not import?
# see https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion
def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string')


def read_description(filename):
    with codecs.open(filename, encoding='utf-8') as f:
        return f.read()


install_requires = [
    'six>=1.9.0'
]

setup(
    name='pystock-client',
    version=find_version('pystock', '__init__.py'),
    url='https://github.com/eliangcs/pystock-client',
    description='Quantitative analysis with Python',
    long_description=read_description('README.rst'),
    author='Chang-Hung Liang',
    author_email='eliang.cs@gmail.com',
    license='MIT',
    packages=['pystock'],
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
