#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    int x, y, sum;


    printf("What's x? ");
    scanf("%d", &x);
    printf("What's y? ");
    scanf("%d", &y);
    printf("%d %d\n", x, y);

    sum = x + y;

    printf("%d\n", sum);

    // compare 
    if (x < y)
    {
        printf("x is less than y\n");
    }
    else if (x > y)
    {
        printf("x is greater than y\n");
    }
    else 
    {
        printf("x and y equal\n");
    }

    return 0;
}