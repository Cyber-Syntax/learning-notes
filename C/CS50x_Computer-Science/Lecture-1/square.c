#include <stdio.h>

int main(void)
{
    // do while to handle negative numbers.
    int column, row;
    do
    { 
    printf("Enter a row: ");
    scanf("%i", &row);

    printf("Enter a column: ");
    scanf("%i", &column);

    } while ( row < 0 || column < 0);
    
    // create square
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < column; j++)
        {
            printf("#");
        }
        printf("\n");
    }


    return 0;
}