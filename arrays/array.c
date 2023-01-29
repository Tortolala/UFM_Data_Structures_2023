#include <stdio.h>

int main()
{
    int arr[5] = {1, 2, 3, 4, 5}; // Array declaration
    int i; 

    printf("Counter i is in address: %d\n", (int) &i); // Prints menmory address of counter i
    for (i = 0; i < 5; i++) // Prints memory address of each element
    {
        // printf("Element %d is in address: %p\n", arr[i], (void *) &arr[i]);
        printf("Element %d is in address: %d\n", arr[i], (int) &arr[i]);
    }
}
