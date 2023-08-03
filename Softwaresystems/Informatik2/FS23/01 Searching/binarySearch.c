#include <stdio.h>
#include <math.h>

void binarySearch(int arr[], int l, int r, int key){
    
    if(r-l >= 1){
        int mid = (l + r)/ 2;

        if(arr[mid] == key){
            printf("The item you're looking for is at index number: %d", mid);
            return;
        }

        if(arr[mid] > key){
            return binarySearch(arr, l, mid-1, key);
        }

        return binarySearch(arr, mid+1, r, key);
    }


    printf("Item was not found in the given array!\n");
    return;
}

int main(){

    int arr[] = { 1, 2, 3, 4, 5, 6};
    int brr[] = {2, 7};
    int n = sizeof(brr) / sizeof(brr[0]);

    binarySearch(brr, 0, n, 25);
}