import sqlines

if __name__ == "__main__":
    # extern int ConvertSql(void *parser, const char *input, int size, const char **output, int *out_size, int *lines);
    # parser = sqlines.CreateParserObject()
    # result = "select * from aip"
    # code = sqlines.ConvertSql(parser,"select * from aip",4000,result,None,None)
    sqlines.translate("select * from aip", sqlines.SQL_MYSQL, sqlines.SQL_ORACLE)
