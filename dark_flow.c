#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

int main(int argc,char** argv){
	// step 1: parse command line
	if((argc<2) || (argc<3)) {
		fprintf(stderr,"usage:%s <function>\n",argv[0]);
		return 0;
	}

	char* cfg_path=find_arg(argc,argv,"-cfg",0);
	printf("the address of cfg is %p\n",cfg_path);
	printf("the cfg is %s\n",cfg_path);

	// step 2: parse cfg file
	FILE* fp=fopen(cfg_path,"r");
	if(fp==0){
		fprintf(stderr,"cfg file:%s open fail!\n",cfg_path);
		return 0;
	}

	char* line;
	//line=fgetl(fp);
	while(line=fgetl(fp)){
		//printf("%s\n",line);
	}	

	fclose(fp);
	
	return 0;
}
