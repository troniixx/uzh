#include <stdio.h>

int A[] = {4, 2, 6, 1, 8, 5};
int c = 9;
int n = sizeof(A)/sizeof(int);
int i, j;
int temp;


//O(n) runtime
void printArrays(int A[], int n){
    for(i = 0; i < n; i++){
        printf("%i ", A[i]);
    }
    printf("\n");
}

//O(n^2)
void bubbleSort(int A[], int n){
    for(i = 0; i < n; i++){
        for(j = 0; n - i; j++){
            if(A[i] > A[i + 1]){ 
                temp = A[i];
                A[i] = A[i + 1];
                A[i + 1] = temp;
            }
        }
    }
}

void pairSum(int A[], int c, int n){
    for(i = 0; i < n; i++){
        for(j = 1; j < n; j++){
            if(A[i] + A[j] == c) {
                printf("%i and %i\n", A[i], A[j]);
            }
        }
    }
}

void pairSumSorted(int A[], int c, int n){
    bubbleSort(A, n);
    for(i = 0; i < n; i++){
        for(j = 1; j < n; j++){
            if(A[i] + A[j] == c) {
                printf("%i and %i\n", A[i], A[j]);
            }
        }
    }
}

int main(){

    printf("pairSum:\n");
    pairSum(A, c, n);

    printf("pairSumSorted:\n");
    pairSumSorted(A, c, n);
    }
