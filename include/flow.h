#ifndef FLOW_API
#define FLOW_API
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node{
	void *val;
	struct node *next;
	struct node *prev;
}node;


typedef struct list{
	int size;
	node *front;
	node *back;
}list;


typedef struct section{
	char *type;
	list *options;
}section;

typedef struct kvp{
	char *key;
	char *val;
	int used;
}kvp;

#endif
