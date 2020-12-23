#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "flow.h"
#include "utils.h"

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

	list *options=make_list();
	section *current;
	char* line;
	line=fgetl(fp);
	strip(line);
	switch(line[0]){
		case '[':
			current=(section*)malloc(sizeof(section));
			list_insert(options,current);
			
	}	
	/*while(line=fgetl(fp)){
		//printf("%s\n",line);
	}*/	

	fclose(fp);
	
	return 0;
}
