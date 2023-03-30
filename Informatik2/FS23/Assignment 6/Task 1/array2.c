#include <stdlib.h>
#include <stdio.h>

void printArray(int arr[], int n){
    for(int i = 0; i < n; i++){
        printf("%d ", arr[i]);
        }
        printf("\n");
}

void swap(int *p, int id1, int id2){
    *(p+id1) += *(p+id2);
    *(p+id2) = *(p+id1) - *(p+id2);
    *(p+id1) = *(p+id1) - *(p+id2);
}

int main(){
    int a[8] = {2, 0, 2, 3, 0, 5, 2, 6};
    swap(a, 2, 3);
    printArray(a, 8);
    return 0;
}