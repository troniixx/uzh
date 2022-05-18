#include <stdio.h>

int search(int A[], int n){
    int max = A[0];

    for(int i = 0; i < n; i++){
        if(A[i] > max){
            max = A[i];
        }
    }

    return max;
}   

int main(){

    int A[] = {1, 2, 3, 4, 5, 7, 9, 6, 3};
    int n = sizeof A / sizeof A[0];
    int sol = search(A, n);

    printf("The largest integer in the given array is: %d", sol);
}