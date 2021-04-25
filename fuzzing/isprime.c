/*
	Checks to see if a number (from user input) is prime

	@author		Sarah Stepak
	@program	isprime.c
	@since		04.25.2021	
*/

#include <stdio.h>
int main() {
	int num = 0;
	int i = 0;
	int isPrime = 0;

	printf("Please enter a positive int: ");
	scanf("%d", &num);

	if (num==1){
	  printf("Neither");
	}
	else {
	  for(i=2; i<=num/2; ++i){
	    if(num%i==0){
	      isPrime=1;
	      break;
	    }
	  }
	  if(isPrime==1){
	  	printf("%d is prime", num);
	  }
	  else{
	  	printf("%d is NOT prime", num);
	  }
	}
	return 0;
}