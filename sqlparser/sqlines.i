%module sqlines

%include "std_string.i"
 
std::string translate(const std::string &input, short source, short target);


%{
#include "sqlparserexp.h"
%}


// SQL dialect types
#define SQL_SQL_SERVER			1
#define SQL_ORACLE				2
#define SQL_DB2					3
#define SQL_MYSQL				4
#define SQL_POSTGRESQL			5
#define SQL_SYBASE				6
#define SQL_INFORMIX			7
#define SQL_GREENPLUM			8
#define SQL_SYBASE_ASA			9
#define SQL_TERADATA			10
#define SQL_NETEZZA				11
#define SQL_MARIADB             12
#define SQL_HIVE				13
#define SQL_REDSHIFT			14
#define SQL_ESGYNDB             15
#define SQL_SYBASE_ADS          16
#define SQL_MARIADB_ORA         17

extern void* CreateParserObject();
extern void SetParserTypes(void *parser, short source, short target);
extern int SetParserOption(void *parser, const char *option, const char *value);
extern int ConvertSql(void *parser, const char *input, int size, const char **output, int *out_size, int *lines);
extern void FreeOutput(const char *output);
extern int CreateAssessmentReport(void *parser, const char *summary);