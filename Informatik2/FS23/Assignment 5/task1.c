#include <stdio.h>
#include <stdlib.h>

void buildMaxHeap(int A[], int n, int d); void printHeap(int A[], int n); void heapSort(int A[], int n, int d); void printArray(int A[], int n); void swap(int *a, int *b);

int main(){
    int A[] = {6, 4, 3, 9, 5, 10, 15, 19, 11, 7, 8, 13};
    int n = sizeof(A) / sizeof(A[0]);
    int d = 3;
}

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void printArray(int A[], int n){
    for(int i = 0; i < n; i++){
        printf("%d ", A[i]);
        }
    printf("\n");
}

void buildMaxHeap(int A[], int n, int d){

}

void printHeap(int A[], int n){
}

void heapSort(int A[], int n, int d){
    
}
