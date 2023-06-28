
import sysconfig

from setuptools import Extension, setup

language = "c++"
std = "c++17"

default_compile_args = sysconfig.get_config_var("CFLAGS").split()
extra_compile_args = [f"-std={std}"]

print(f"Default compile arguments: {default_compile_args}")
print(f"Extra compile arguments: {extra_compile_args}")

extension = Extension(
    "sqlines",
    sources=[
        "sqlparser/sqlines_wrap.cpp",
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
    extra_compile_args=extra_compile_args,
    language=language,
)

setup(
    name="sqlines",
    version="1.0",
    description="This is Example module written in C++",
    ext_modules=[extension],
)
