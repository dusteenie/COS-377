/*
 	@author:	Sarah Stepak	
 	@date:		02.09.2021
 	@program:	CNotes_Basics-Datatypes-Operators.c
 	@purpose:	Inital C notes

	-------------------------------------------------------------
	-------------------------------------------------------------
*/


/*

	CLASS NOTES: 
	-------------------------------------------------------------
	-------------------------------------------------------------


	data types
	-------------------------------------------
	short, int, long. (Can also do unsigned int)
	float, double
	char
	char *	(pointer var)


	Operators
	-------------------------------------------
	Arithmetic,	Relatioal,	Boolean
	*	(de-refrences pointer var)
	Pointer (*) / Refrence (&)


	Sizes of a 32 bit system
	-------------------------------------------
	bit
	nibble (4bits)
	byte (2 nibbles, or 8 bits)
	word (2bytes, or 16 bits)
	DWORD (2 words)
	QWORD (4 words)
*/


/*
	Class Code
	-------------------------------------------------------------
	-------------------------------------------------------------
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int foo();


void greeting(char * temp1, char * temp2){
	char name[400];
	strcpy(name, temp2);
	printf("hello %s %s \n", temp1, name);
}

int main(int argc, char * argv[]){


	greeting(arg[1], arg[2]);
	printf("Bye %s %s\n", arg[1], arg[2]);

	// Printing User Input
	int number;
	scanf("%d",&number);
	printf("You typed: %d",number);

	// Memory Allocation
	char * s1 = "banana";
	char * s2 = "apple";
	// the dollowing allocates the size of a char times 10.
	// it then casts the return to char.
	char * s3 = (char *) malloc(sizeof(char)*10);


	// Loops
	while(i < 20){
		printf("%d\n,"i);
		i++; }
	for(int j = 1; j<10; j++){
		printf("%d\n,"j); }


	// Print Statement
	printf("hello");

	// Function Call
	foo();

	// Exit on Success
	exit(0);
}

int foo(void){
	printf(" world!");
}

