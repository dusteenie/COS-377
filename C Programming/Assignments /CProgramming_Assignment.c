/*
	@author:	Sarah Stepak
	@date:		03.27.2021
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
int stringLen( char * s)
{
	int i = 0;
	while (s[i]){
		i++;
	}
	return i;
}


/*
	This function is used to concatenate two strings togtether.
	    It does not use strcat()
	@param	a	Type: char *, contains the first string
	@param	b	Type: char *, contains the second string
	@return		Type: char *,	Returns the concatonated string.
*/
char * concatenate(char * a, char * b)
{
	int len = stringLen(a) + stringLen(b);
	char * result = (char *) malloc(len);
	
	int pos = 0;
	int i = 0;
	while(a[i]){
		result[pos] = a[i];
		i++;
		pos++;
	}

	i=0;
	while(b[i]){
		result[pos] = b[i];
		i++;
		pos++;
	}

	return result;

}

/*
	This function replaces all occurrences of a character in a string 
	with another character. 
	@param	s	Type: char *, contains first string
	@param	a	Type: char, contains the char we want to replace
	@param	b	Type: char, contains the char we will replace a with
	@return		Type: char *,  returns the new string.
*/
void replace(char * s, char a, char b)
{
	int i = 0;
	while(s[i])
	{
		if( s[i] == a)
		{
			s[i] = b;
		}

		i++;
	}

	printf("New String: %s \n", s);
}


// Main method
int main(int argc, char * argv [])
{

	// String declaration (of up to 100 chars)
	// s1 - String 1, s2 - String 2
	char * s1[100];
	char * s2[100];
	char c1,c2;

	// Prompts the user for input
	printf("Please input the first string:  ");
	scanf("%s",&s1);
	printf("Please input the second string:  ");
	scanf("%s",&s2);
	printf("Input char to be replaced:  ");
	scanf(" %c",&c1);	
	printf("Input char to replace:  ");
	scanf(" %c",&c2);	
	printf("\n\n");

	// Calls the first function
	int lenS1 = stringLen(s1);
	int lenS2 = stringLen(s2);
	printf("Length of String 1:  ");
	printf("%d",lenS1);
	printf("\nLength of String 2:  ");
	printf("%d",lenS2);
	printf("\n\n");

	// Calls the second function
	printf("String 1 concat String 2:  ");
	printf("%s",concatenate(s1,s2));
	printf("\nString 2 concat String 1:  ");
	printf("%s",concatenate(s2,s1));
	printf("\n\n");

	// Calls the last function
	printf("Replacing the letter in String 1:  \n");
	replace(s1,c1,c2);
	printf("Replacing the letter in String 2:  \n");
	replace(s2,c1,c2);
}