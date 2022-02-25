#include <stdio.h>

// swap the the position of two elements
void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

//sort
void selectionSort(int array[], int size) {
    for (int step = 0; step < size - 1; step++) {
    int min_idx = step;
    for (int i = step + 1; i < size; i++) {

      // To sort in descending order, change > to < in this line.
      // Select the minimum element in each loop.
    if (array[i] < array[min_idx])
        min_idx = i;
    }

    // put min at the correct position
    swap(&array[min_idx], &array[step]);
    }
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

    selectionSort(data, size);
    
    printf("Sorted Array:\n");
    printArray(data, size);
}