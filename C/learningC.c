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

	// Basic Data Types: character (char), integer (int), float (float), double (double)
	// A float has less precision than a double, 6 vs 15 possible decimal places respectively.
	// As a result, double takes up more memory than float data type so double is faster.

	// Way to declare variable with float data type
	float x = 1.2345f;
	
	// Way to declare variable with double data type
	double y = 2.1325;

	printf("My age is %d years old.\n", age); // in place of %d, we can also write %i

	printf("My favourite number is %c!\n", favouriteNumber);
	printf("My favourite letter is %c!\n", favouriteLetter);
	printf("%f\n", x);
	printf("%f\n", y);
	return 0;
}