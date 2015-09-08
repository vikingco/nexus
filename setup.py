#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


setup(
    name='nexus',
    version='0.3.1+yplan1',
    author='Disqus',
    author_email='opensource@disqus.com',
    url='https://github.com/disqus/nexus',
    description='An extendable admin interface',
    packages=find_packages(exclude=['example_module', 'tests']),
    zip_safe=False,
    install_requires=[],
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
