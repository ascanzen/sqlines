#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Setup this SWIG library."""
import runpy

from setuptools import Extension, find_packages, setup
from setuptools.command.build_py import build_py

STD_EXT = Extension(
    name='sqlines',
    swig_opts=['-c++'],
    sources=[
        "sqlparser/sqlines.i",
        "sqlparser/clauses.cpp",
        "sqlparser/guess.cpp",
        "sqlparser/post.cpp",
        "sqlparser/stats.cpp",
        "sqlparser/cobol.cpp",
        "sqlparser/helpers.cpp",
        "sqlparser/postgresql.cpp",
        "sqlparser/storage.cpp",
        "sqlparser/datatypes.cpp",
        "sqlparser/informix.cpp",
        "sqlparser/procedures.cpp",
        "sqlparser/str.cpp",
        "sqlparser/db2.cpp",
        "sqlparser/java.cpp",
        "sqlparser/report.cpp",
        "sqlparser/sybase.cpp",
        "sqlparser/dllmain.cpp",
        "sqlparser/language.cpp",
        "sqlparser/select.cpp",
        "sqlparser/teradata.cpp",
        "sqlparser/file.cpp",
        "sqlparser/mysql.cpp",
        "sqlparser/sqlparser.cpp",
        "sqlparser/token.cpp",
        "sqlparser/functions.cpp",
        "sqlparser/oracle.cpp",
        "sqlparser/sqlserver.cpp",
        "sqlparser/greenplum.cpp",
        "sqlparser/patterns.cpp",
        "sqlparser/statements.cpp",
   
    ],
    include_dirs=[
        'sqlparser',
    ],
    extra_compile_args=[  # The g++ (4.8) in Travis needs this
        '-std=c++17',
    ]
)


# Build extensions before python modules,
# or the generated SWIG python files will be missing.
class BuildPy(build_py):
    def run(self):
        self.run_command('build_ext')
        super(build_py, self).run()


INFO = runpy.run_path('sqlparser/_meta.py')

setup(
    name='sqlines',
    description='A Python wrapper for sqlines',
    version=INFO['__version__'],
    author=INFO['__author__'],
    license=INFO['__copyright__'],
    author_email=INFO['__email__'],
    url=INFO['__url__'],
    keywords=['sqlines'],

    packages=find_packages('sqlines'),
    package_dir={'': 'sqlines'},
    package_data={'': ['*.pyd']},
    ext_modules=[STD_EXT],
    cmdclass={
        'build_py': BuildPy,
    },

    python_requires='>=3.1',
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-flake8',
    ],    
)