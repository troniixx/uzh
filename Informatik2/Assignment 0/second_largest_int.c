#include <stdio.h>

int main() {

    int i, j, temp;
    int Arr[] = {0, 1, 2, 3, 4, 5, 6, 7};
    int n = 8;
    
    /* first sort the array from largest to smallest and then output the second number */

    /* sort */
    for(i = 0; i < n; ++i){
        for(j = i + 1; j < n; ++j) {
            if (Arr[i] < Arr[j]) {
                temp = Arr[i];
                Arr[i] = Arr[j];
                Arr[j] = temp;
            }
        }
    }

    /* print the array */
    printf("Sorted array: ");
    for(i = 0; i < n; ++i) {
        printf("%d ", Arr[i]);
    }
    printf("\n");

    /* print the result */
    printf("The second largest integer in the array is: %d\n", Arr[1]);

}