#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(void)
{
    char c[2];
    printf("Do you agree? "); // you must use "" double quotes when it's sentences...
    fgets(c, 2, stdin);
    
    char lowerC = tolower(c[0]); //convert input to lowercase

    if (lowerC == 'y') // you must use '' single quotes when it's char.
    {
        printf("Agreed.\n");
    }
    else if (lowerC == 'n')
    {
        printf("Not agreed.\n");
    }

    // Exit the program with a status code of 0 to indicate(belirtmek) success
    return 0;
}
