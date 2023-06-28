%module sqlines

%{
#include <stdlib.h>
%}

// Now list ISO C/C++ declarations

void* CreateParserObject();

void SetParserTypes(void *parser, short source, short target);

int ConvertSql(void *parser, const char *input, int size, const char **output, int *out_size, int *lines);

int SetParserOption(void *parser, const char *option, const char *value);

// Create report file
int CreateAssessmentReport(void *parser, const char *summary);
// Free allocated result
void FreeOutput(const char *output);

