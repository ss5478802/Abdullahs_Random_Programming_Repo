#include <stdio.h>

// Trying to learn C!

int main(){
	
	printf("My name is Abdullah!\n");
	
	// This is a constant and this is the only way to declare constant 
	const int age = 15;
	
	// This is a variable. This is one way of declaring variables
	char favouriteNumber = '5';
	
	// This is another way of declaring variables
	char favouriteLetter;
	favouriteLetter = 'A';

	printf("My age is %d years old.\n", age); // in place of %d, we can also write %i

	printf("My favourite number is %i!\n", favouriteNumber);
	printf("My favourite letter is %c!\n", favouriteLetter);
	return 0;
}