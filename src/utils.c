#include <stdio.h>
#include <stdlib.h>
#include <string.h>


list *make_list(){
    list *tmp;
    tmp=(list*)malloc(sizeof(list));
    tmp->size=0;
    tmp->fornt=0;
    tmp->back=0;

    return tmp;
}

void strip(char *line){

}

char* find_arg(int argc,char** argv,char* option,char* value){
    char* str;
    for(int i=0;i<argc-1;i++){
        if(0==strcmp(argv[i],option)){
            str= argv[i+1];
            return str;
        }
    }
    return value;
}


char* fgetl(FILE* fp){
    if(feof(fp)) return 0;
    size_t size=512;
    char* line=malloc(size*sizeof(char));
    //printf("before: %p\n",fp);
    if(!fgets(line,size,fp)){
        free(line);
        return 0;
    }
	//printf("after: %p\n",fp);
    //printf("fgetl:%s\n",line);
    size_t curr=strlen(line);
    //printf("the line lenght is %zu\n",curr);
    printf("%s",line);

    return line;
}






