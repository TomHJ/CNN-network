#include "flow.h"



list *make_list();
void strip(char *line);
char* find_arg(int argc,char** argv,char* option,char* value);
char* fgetl(FILE* fp);
void list_insert(list *options,section *current);
