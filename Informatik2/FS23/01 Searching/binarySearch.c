#include <stdio.h>
#include <math.h>

void binarySearch(int arr[], int l, int r, int k){
    
    if(r >= 1){
        int m = l + (r-1) / 2;

        if(arr[m] == k){
            printf("The item you're looking for is at index number: %d", m);
            return;
        }

        if(arr[m] > k){
            return binarySearch(arr, l, m-1, k);
        }
        return binarySearch(arr, m+1, r, k);
    }
    printf("Item was not found in the given array!\n");
    return;
}

int main(){

    int arr[] = { 1, 2, 3, 4, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    binarySearch(arr, 0, n, 5);
}