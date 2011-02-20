#!/usr/bin/env python

METADATA = dict(
    name='django-panoramio',
    version='0.1',
    author='ramusus',
    description='Django application for interacting with Panoramio images through python-panoramio library',
    long_description=open('README').read(),
    url='http://github.com/ramusus/django-panoramio',
)

if __name__ == '__main__':
    try:
        import setuptools
        setuptools.setup(**METADATA)
    except ImportError:
        import distutils.core
        distutils.core.setup(**METADATA)
