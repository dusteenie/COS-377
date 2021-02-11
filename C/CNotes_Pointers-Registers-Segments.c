/*
	@author:	Sarah Stepak
	@date:		02.11.2021
	@program: 	CNotes_Pointers-Registers-Segments.c

	-------------------------------------------------------------
	-------------------------------------------------------------
*/

/*

	CLASS NOTES: 
	-------------------------------------------------------------
	-------------------------------------------------------------


	Segment
	-------------------------------------------------------------
	[text | .data  | .bss | heap | -->  <-- | stack | enviroment]

	Text is exacutable and readable.
	Data is not. It's only readable.
	.bss is for uninitalized variables.
	heap does up
	stack goes down 

	This enviroment is for the terminal / bash.




	Assembly and Registers 
	-------------------------------------------------------------
	.
	CPU
	|----------------|
	|                |
	|   []  []  []   |
	|   R   R   R    |
	|                |
	|----------------|

	The R is Registers
	.
	.
	[    | heap -> ]
	The first 16 bits give you, and then the next gives you the offset and where you are.
	.
	Special regesters:
	0 Flag - A regester that only holds 0/1 (boolean test)
	[refrence 'cheat sheet for more info']




	AT&T vs NASM 
	-------------------------------------------------------------
	The only difference between the two is that the syntax is switched.
*/




/*
	Class Code
	-------------------------------------------------------------
	-------------------------------------------------------------
*/

// Include statements
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Main method
int main(int argc, char * argv []){
	// NOTES - pointers
	/* 
		Creates a pointer to the char variable
		terminated by \0
			\0 is the NULL char
			(you know you foud the end when you hit \0)
	*/
	char * s; 

	s = "name";
	printf("%s\n",s);
	// if we do printf("%s\n",s*), we get a segmentation fault because it derefs the var
}