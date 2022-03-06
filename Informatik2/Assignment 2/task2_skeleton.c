/****************************************************************************
 * University of Zurich, Informatics II, Spring Semester 2022               *
 * Exercise 2 - Task 2                                                      *
 *                                                                          *
 * @author Mert Erol                                                        *
 ****************************************************************************/

#include <stdio.h>

// hard-coded maximum length for input strings
const int MAX_LENGTH = 1000;

void insertionSort(int arr[], int i, int n) {

    int value = arr[i];
    int j = i;

	while (j > 0 && arr[j - 1] > value)
    {
        arr[j] = arr[j - 1];
        j--;
    }
	arr[j] = value;

	if (i + 1 <= n) {
        insertionSort(arr, i + 1, n);
    }

}

int main() {
	printf("Values of array separated by spaces (non-number to stop): ");
	int arr[MAX_LENGTH];
	int pos = 0;
	while (scanf("%d", &arr[pos]) == 1) {
		pos++;
	}
	// variable pos will contain number of integers read in from user

	// TODO: your implementation
	int n = sizeof(*arr)/sizeof(arr[0]);
	insertionSort(arr, 1, n-1);
	printf("The second smallest number is %d", arr[1]);

	return 0;
}
