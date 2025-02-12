#include <stdio.h>

int main(void)
{
    
    // repeat meow 3 times
    for (int i = 0; i < 3; i++)
    {
        printf("meow\n");
    }
    // repeat cow 3 times but more efficient way    
    for (int i = 1; i <= 3; i++)
    {
        printf("mooo\n");
    }
    
    // Let we do this with while loop
    int i = 0;
    while (i < 3)
    {
        printf("roar\n");
        i++;
    }


    return 0;

}
