#include <stdio.h>

void printer(int arr[], int n){
    for(int i = 0; i < n; i++){
        printf("%d ", arr[i]);
    }
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void selectionSort(int arr[], int n){
    for(int i = 0; i < n - 1; i++){
        int min = i;
        for(int j = i + 1; j < n; j++){
            if(arr[j] < arr[min]){
                min = j;
            }
        }
        //swapping using pointers
        swap(&arr[min], &arr[i]);

        //alternative way wihtout the usage of pointers
        //int temp = arr[min];
        //arr[min] = arr[i];
        //arr[i] = temp;
    }
}

int main(){
    int arr[5] = {3, 7, 1, 12, 9};
    selectionSort(arr, 5);

    printer(arr, 5);

}