#include <stdio.h>
#define MIN -999999999

int main() {
	int n = 5;
	int A[] =  { 11, 3, -3, 2, -5};
	int pos1 = -1, pos2 = -1;
	int target = MIN;
	for(int i = 0; i < n; i++ ) {
		if(A[i] > target) {
			pos1 = i;
			target = A[i];
		}
	}
	target = MIN;
	for(int i = 0; i < n; i++ ) {
		if(i != pos1 && A[i] > target) {
			pos2 = i;
			target = A[i];
		}
	}
	printf("%d\n", A[pos2]);
}