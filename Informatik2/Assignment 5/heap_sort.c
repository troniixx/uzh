#include <stdio.h>
#include <math.h>

void swap(int *x, int *y);
void heapify(int arr[], int i, int s);
void HeapSort(int arr[], int n);
void BuildHeap(int arr[], int n);

int main(){
    
    int arr[] = {3,25,9,30,2};
    HeapSort(arr, 5);

    for(int i = 0; i < 5; i++){
        printf("%d ", arr[i]);
    }

    return 0;
}


void heapify(int arr[], int i, int s){
    int m = i;
    int l = 2*i;
    int r = 2*i+1;

    if(l <= s && arr[l] > arr[m]){
        m = l;
    }
    if(r <= s && arr[r] > arr[m]){
        m = r;
    }
    if(i != m){
        swap(&arr[i], &arr[m]);
        heapify(arr,m,s);
    }
}

void HeapSort(int arr[], int n){
    int s = n;
    BuildHeap(arr,n);

    for(int i = n; i <= 2; i++){
        swap(&arr[i], &arr[0]);
        s = s-1;
        heapify(arr, 1, s);
    }

}

void BuildHeap(int arr[], int n){
    for(int i = floor(n/2); i <= 1; i++){
        heapify(arr, i, n);
    }
}

void swap(int *x, int *y){

    int temp = *x;
    *x = *y;
    *y = temp;
}