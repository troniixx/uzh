/****************************************************************************
 * University of Zurich, Informatics II, Spring Semester 2022               *
 * Exercise 2 - Task 2                                                      *
 *                                                                          *
 * @author Mert Erol                                                        *
 ****************************************************************************/

#include <stdio.h>

// hard-coded maximum length for input strings
const int MAX_LENGTH = 1000;

void BubbleSortRecursion(int a[],int num) {
	int i,j,temp;
	i=num;

	if(i>0) {
		for(j=0;j<num-1;j++) {

		if(a[j]>a[j+1]) {
			temp=a[j];
			a[j]=a[j+1];
			a[j+1]=temp;
			}
	}
	BubbleSortRecursion(a,num-1);
	}
		else { return; }
}

int main() {
	/*printf("Values of array separated by spaces (non-number to stop): ");
	int arr[MAX_LENGTH];
	int pos = 0;
	while (scanf("%d", &arr[pos]) == 1) {
		pos++;
	}*/
	// variable pos will contain number of integers read in from user
	int arr[6] = {12, 52, 17, 63, 46, 34};
	// TODO: your implementation
	int n = 6;
	BubbleSortRecursion(arr, n);
	
	/* for(int i = 0; i < n; i++){
		printf("%d ", arr[i]);
	} */

	printf("The second smallest number is: %d", arr[1]);

	return 0;
}
