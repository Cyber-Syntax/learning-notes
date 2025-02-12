#include <stdio.h>
#include <stdlib.h>

void ask_user(char *word, int number);
void repeat(char *word, int number);

int main(void)
{
    // use functions to make the code more readable
    char *word = malloc(10* sizeof(char)); // allocate memory for the word
    int number; // number of times to repeat the word

    ask_user(word, number);
    repeat(word, number);

    free(word); // free the memory allocated for the word
    
    return 0;
}

void repeat(char word[10], int number)
{
    // repeat the word for the number of times
    for (int i = 0; i < number; i++)
    {
        printf("%s", word);
    }
}

void ask_user(char word[10], int number)
{
    // ask user for a word
    printf("Enter a word: ");
    scanf("%s", word);

    // ask user for a number
    printf("Enter a number:");
    scanf("%i", &number);

}