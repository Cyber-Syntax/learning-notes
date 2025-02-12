#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    // Declare a char array to hold the user's name
    char name[100];

    // Ask the user for their name and read it from standard input
    printf("Please enter your name: ");
    fgets(name, 100, stdin); // stdin allowing user to enter data
                             // into the program via the command line
    
    // Print a personalized greeting using the user's name
    printf("Hello, %s!\n", name); // %s is a format specifier used in `printf` and related functions to format and print strings.    

    // Exit the program with a status code of 0 to indicate(belirtmek) success
    return 0;
}
