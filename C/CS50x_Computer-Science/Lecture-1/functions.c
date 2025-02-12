#include <stdio.h>

int main(void)
{
    struct repeat
    {
        char *word;
        int times;
    };

    // ask user for a word
    char word[10];
    printf("Enter a word: ");
    scanf("%s", word);

    // ask user for a number
    int number;
    printf("Enter a number: ");
    scanf("%i", &number);

    // repeat the word for the number of times
    for (int i = 0; i < number; i++)
    {
        printf("%s\n", word);
    }
    
    
}

    
