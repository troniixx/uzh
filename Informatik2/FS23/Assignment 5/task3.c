#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int* arr, int left, int right, int* pivot_left){
    if(arr[left] > arr[right]){
        swap(&arr[left], &arr[right]);
    }

    int j = left+1;
    int k = right-1;
    int l = left+1;

    int p1 = arr[left]; //left pivot
    int p2 = arr[right]; //right pivot

    while(l <= k){

        //element less than left pivot
        if(arr[l] < p1){
            swap(&arr[l], &arr[j]);
            j++;
        }

        //element greater equal to right pivot
        else if(arr[l] >= p2){
            while(arr[k] > p2 && l < k){
                k--;
            }
            swap(&arr[l], &arr[k]);
            k--;
            if(arr[l] < p1){
                swap(&arr[l], &arr[j]);
                j++;
            }
        }
        l++;
    }
    j--;
    k++;

    swap(&arr[left], &arr[j]);
    swap(&arr[right], &arr[k]);
    *pivot_left = j;

    return k;
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

void printArray(int arr[], int n){
    for(int i = 0; i < n; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main(){
    int arr[] = { 24, 8, 42, 75, 29, 77, 38, 57 };
    quicksort(arr, 0, 7);
    printArray(arr, 7);
    
    return 0;
}