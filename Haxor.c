/*
	@author:	Sarah Stepak
	@date:		02.11.2021
	@program: 	Haxor.c

	-------------------------------------------------------------
	-------------------------------------------------------------
*/

/*
	To run:
	gcc -ggdb -o hax Haxor.c
	gdb hax

	GDB NOTES
	info b   - shows breakpoint info
	info r   - shows regester info
	in    - shows the next item
	quit   - kills process

	set disassembly-flavor intel
	disassemble hax    - shows the assembly dump
*/

// Include statements
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Main method
int main(int argc, char * argv []){
	printf("%s\n", "Hello Haxor");
}