# SQLines SQL Converter

SQLines SQL Converter is an open source tool (Apache License 2.0) that allows you to convert database schema (DDL), queries and DML statements, views, stored procedures, packages, functions and triggers between Microsoft SQL Server, Oracle, MariaDB, MySQL, PostgreSQL, IBM DB2, Sybase, Informix, Teradata, Greenplum and Netezza.

You can also try it online at <http://www.sqlines.com/online>

## Build SQLines SQL Converter

The first step is to build SQLParser:

```sh
cd sqlparser
./build_all64.sh
```

## Support

For technical support and custom development, please contact us at <support@sqlines.com>

## 编译注意事项

### Mac下编译，设置Python.h 目录

sudo find / -iname "Python.h"
export CPLUS_INCLUDE_PATH="/usr/local/Cellar/python@3.9/3.9.17_1/Frameworks/Python.framework/Versions/3.9/include/python3.9"

### swig问题

sqlines.py生成文件中 _sqlines 需要手动改为 sqlines，否则会将Pyinit_sqlines接口写在 Pyinit__sqlines.
