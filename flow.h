#ifndef FLOW_API
#define FLOW_API
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct kvp{
	char *key;
	char *val;
	int used;
}kvp;


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

#endif
