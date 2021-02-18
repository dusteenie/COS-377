/*
	@author:	Sarah Stepak
	@date:		02.11.2021
	            DUE: 02.15.2021
	@program: 	CProgramming_Assignment.c


	Assignment Details

	Creates a C program with functions for each of the following:
	    Find the length of a string 
	    	int strLength(char * s)

	    Concatenate two strings together. The function should receive 
	    two strings and return a single string. You may not use strcat() function. 
	    	char * concatenate(char * a, char * b)

	    Replace all occurrences of a character in a string with another character.
	    	void replace(char * s, char a, char b)

	-------------------------------------------------------------

	To run

	gcc [programName].c -o programName
	./programName

	-------------------------------------------------------------
	-------------------------------------------------------------
*/

// Include statements
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



/*
	This function is used to return the length of a string.
	@param	s	Type: char, contains the string
	@return		Type: int,	Returns the length of the string.
*/
int stringLen( char * s){
	int i;
	//add loop
	//s[i]
	//*[s+i]
}


/*
	This function is used to concatenate two strings togtether.
	    It does not use strcat()
	@param	a	Type: char *, contains the first string
	@param	b	Type: char *, contains the second string
	@return		Type: char *,	Returns the concatonated string.
*/
char * concatenate(char * a, char * b){}

/*
	This function is used to concatenate two strings togtether.
	    It does not use strcat()
	@param	s	Type: char *, contains the first string
	@param	name	Type: char, contains the second string
	@return			Type: char,	Returns the concatonated string.
*/
void replace(char * s, char a, char b){}


// Main method
int main(int argc, char * argv []){

	/* 
		Declares Vars
		-------------------------------------
	*/

	// String declaration (of up to 100 chars)
	// s1 - String 1, s2 - String 2
	char s1[100];
	char s2[100];

	// Length of strings
	int lenS1;
	int lenS2;


	// Prompts the user for input
	printf("Please input the first string: \n");
	scanf("%s",s1);
	printf("Please input the second string: \n");
	scanf("%s",s2);	
	printf("\n\n");
	//("%s",s1); DEBUG

	// Calls the first function
	printf("Length of String 1: \n");
	printf("Length of String 2: \n");
}