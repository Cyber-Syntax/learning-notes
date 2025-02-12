#include <stdio.h>

int main(void)
{
    // Creating a square but like this:
    // \_______/
    // |       |
    // |       |
    // |       |
    // |_______|
    // /       \

    // just lest do this square in a simple way like above
    // without asking user

    // create square
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if (i == 0 || i == 4)
            {
                printf("_");
            }
            else if (j == 0 || j == 9)
            {
                printf("|");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }


    return 0;
}