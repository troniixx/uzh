#include <stdio.h>

void printer(int arr[], int n){
    for(int i = 0; i < n; i++){
        printf("%d ", arr[i]);
    }
}

void insertionSort(int arr[], int n){
    for(int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        while(key < arr[j] && j >= 0){
            arr[j+1] = arr[j];
            --j;
        }
        arr[j+1] = key;
    }
}

int main(){
    int arr[5] = {3, 7, 1, 12, 9};
    insertionSort(arr, 5);

    printer(arr, 5);

}
