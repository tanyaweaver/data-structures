# -*- coding: utf -8*-
from setuptools import setup

setup(
    name="linked list, stack, double linked list, queue, deque implementation",
    description="This package implements a linked list",
    version=0.1,
    license='MIT',
    author="Steven Than, Tatiana Weaver",
    author_email="email@email.com",
    py_modules=['linked_list', 'stack', 'dll', 'queue', 'deque'],
    package_dir={' ': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
)
