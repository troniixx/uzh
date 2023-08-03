#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int l, int r) {
    int p = arr[l];
    int i = l + 1;
    int j = r;

    while (i <= j) {
        while (i <= j && arr[i] <= p) {
            i++;
        }
        while (i <= j && arr[j] > p) {
            j--;
        }
        if (i < j) {
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[l], &arr[j]);

    return j;
}

void quicksort(int arr[], int l, int r){
    if(l >= r){
        return;
    }

    int p = partition(arr, l , r);

    quicksort(arr, l, p);
    quicksort(arr, p+1, r);
}

void printArray(int arr[], int n){
    for(int i = 0; i < n; i++){
        printf("%d ", arr[i]);
    }
}

int main(){
    int n = 6;
    int m = n-1;
    int arr[] = {1, 32, 23, 15, 19, 69};

    printf("Before sorting: \n");
    printArray(arr, n);
    printf("\n");
    printf("After sorting: \n");
    quicksort(arr, 0, m);
    printArray(arr, n);





    return 0;
}