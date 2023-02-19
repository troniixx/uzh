#include <stdio.h>

int insertionSort(int array[], int size) {

}

void printArray(int array[], int size) {

    for (int i = 0; i < size; ++i) {
        printf("%d  ", array[i]);
        }

    printf("\n");
}

int main() {

    int data[] = {-2, 45, 0, 11, -9};
    int size = sizeof(data) / sizeof(data[0]);

    insertionSort(data, size);
    
    printf("Sorted Array:\n");
    printArray(data, size);
}