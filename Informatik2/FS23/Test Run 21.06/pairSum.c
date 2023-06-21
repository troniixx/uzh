#include <stdio.h>
#include <stdlib.h>

int pairSum(int arr[], int c, int n){
    for(int i = 0; i < n; i++){
        for(int j = 1; j < n; j++){
            if(arr[i] + arr[j] == c){
                printf("Pair found!");
                return 1;
            }
        }
    }

    printf("No pair found!");
    return 0;
}

int main(){
    int arr[10] = {1, 2, 3, 4, 5, 6, 12, 8, 9, 10};
    int n = 10;
    int noPair = 69;
    int pair = 7;

    printf("Next line should be 'No pair found!'\n");
    pairSum(arr, noPair, n);
    printf("\n");
    printf("Next line should be 'Pair found!'\n");
    pairSum(arr, pair, n);
    

    return 0;
}
