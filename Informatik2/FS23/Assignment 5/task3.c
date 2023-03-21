#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int* arr, int left, int right, int pivot_left){
    if(arr[left] > arr[right]){
        swap(&arr[left], &arr[right]);
    }

    int j = left+1;
    int k = right-1;
    int l = left+1;

    int p1 = arr[left]; //left pivot
    int p2 = arr[right]; //right pivot
}

void quicksort(int* arr, int left, int right){
    if(left < right){
        int pivot_left, pivot_right;
        pivot_right = partition(arr, left, right, &pivot_left);

        quicksort(arr, left, pivot_left-1);
        quicksort(arr, pivot_left+1, pivot_right-1);
        quicksort(arr, pivot_right+1, right);
    }
}