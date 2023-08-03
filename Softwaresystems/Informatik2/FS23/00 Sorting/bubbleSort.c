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

void bubbleSort(int arr[], int n){
    for(int i = 0; i < n - 1; i++){
        for(int j = 0; j < n - 1 - i; j++){
            if(arr[j] > arr[j + 1]){

                //swapping using pointers
                swap(&arr[j], &arr[j + 1]);

                //alternative way wihtout the usage of pointers
                //int temp = arr[j];
                //arr[j] = arr[j+1];
                //arr[j+1] = temp;
            }
        }
    }
}

int main(){
    int arr[5] = {3, 7, 1, 12, 9};
    bubbleSort(arr, 5);

    printer(arr, 5);

}