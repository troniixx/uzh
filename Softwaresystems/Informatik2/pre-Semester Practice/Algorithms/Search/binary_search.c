#include <string.h>
#include <stdio.h>

int binarySearch(int arr[], int l, int r, int n){
    
    if(r >= l) {
        int mid = l + (r-1)/2;

        if(arr[mid] == n) {
            return mid;
        }

        if (arr[mid] > n) {
            return binarySearch(arr, l, mid - 1, n);
        }

        return binarySearch(arr, mid, r-1, n);
    }

    return -1;
}

int main(void) {
    int arr[] = {5, 210, 124, 122, 5, 89, 1, 2, 19, 69, 420, 31, 2001, 12, 31, 41, 690, 128};
    int n = 31; 
    int r = sizeof(arr)/sizeof(arr[0]); 

    int result = binarySearch(arr, 0, r - 1, n);

    if(result == -1){
        printf("Element is not present in the array");
    } 
    else {
        printf("Element is present at index %d", result);
    }
    return 0;
}