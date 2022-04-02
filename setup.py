#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'graphene-django>=2.13,<3.0.0',
    'django>=3.2.9,<4.0.0',
    # 'django-cors-headers>=3.7,<4.0.0',
]

test_requirements = []

setup(
    author="Matteo Ghia",
    author_email='matteo.ghia@yahoo.it',
    python_requires='>=3.6',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Operating System :: POSIX :: Linux',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    description="GraphQL integration for AllianceAuth",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='allianceauth_graphql',
    name='allianceauth_graphql',
    packages=find_packages(include=['allianceauth_graphql', 'allianceauth_graphql.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Maestro-Zacht/allianceauth-graphql',
    version='0.1.0',
    zip_safe=False,
)
