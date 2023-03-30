#include <stdio.h>
#include <limits.h>

int kth_child(int i,int k,int d){
    return d * i + k;
}

void heapify(int arr[], int n, int i, int d) {
    int largest = i;
    for (int k = 1; k <= d; k++) {
        int child = kth_child(i, k, d);
        if (child < n && arr[child] > arr[largest]) {
            largest = child;
        }
    }
    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest, d);
    }
}

void buildMaxHeap(int A[], int n, int d){
    for (int i = n/d; i > -1; i--){
        heapify(A,n,i,d);
    }
}

void heapSort(int A[], int n, int d){
    buildMaxHeap(A,n,d);
    for(int i = n-1; i > 0; i--){
        int temp = A[i];
        A[i] = A[0];
        A[0] = temp;
        heapify(A,i,0,d);
        
    }
}

void printArray(int A[], int n){

    for(int i = 0; i < n; i++){
        printf("%d ", A[i]);
    }
    
}


int main(){

    int arr[] = {6, 4, 3, 9, 5, 10, 15, 19, 11, 7, 8, 13};
    int n = sizeof(arr) / sizeof(arr[0]); 
    int d = 3;
    printArray(arr,n);
    printf("\n");
    heapSort(arr,n,d);
    printArray(arr,n);
    
    return 0;
}
