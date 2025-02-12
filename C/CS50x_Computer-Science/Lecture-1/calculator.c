#include <stdio.h>

int main(void)
{
    // calculator app
    printf("Welcome to the calculator app!");
    // select case
    printf("Select an operation: 1. Add 2. Subtract 3. Multiply 4. Divide: ");
    int operation;
    scanf("%d", &operation);
    // get numbers
    printf("Enter number 1: ");
    float num1, num2;
    scanf("%f", &num1);
    printf("Enter number 2: ");
    scanf("%f", &num2);
    // perform operation
    float result;

    switch (operation)
    {
        case 1:
            result = num1 + num2;
            printf("Result: %f", result);
            break;
        case 2:
            result = num1 - num2;
            printf("Result: %f", result);
            break;
        case 3:
            result = num1 * num2;
            printf("Result: %f", result);
            break;
        case 4:
            result = num1 / num2;
            printf("Result: %f", result);
            break;
        default:
            printf("Invalid operation!");
            break;
    }

    printf("\n");
    return 0;
    
}