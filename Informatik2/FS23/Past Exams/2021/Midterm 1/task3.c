#include <stdlib.h>
#include <stdio.h>


// arr = given array, n = length of array, left = idx of first element in array, right = idx of last element in array
int apex(int arr[], int n, int left, int right){
    if (right - left <= 1) {
        return -1;  // Base case: not enough elements to form an apex
    }
    
    int smallest = -1;

    if(right-left > 1){

        int mid = (right+left)/2;
        int left_split = apex(arr, n, left, mid);
        int right_split = apex(arr, n, mid+1, right);


        //checking mid
        int check = mid;

        if(arr[check] >= arr[check-1] && arr[check] >= arr[check+1]){
            if(left_split == -1 || arr[left_split] > arr[check]){
                left_split = check;
            }
        }


        //checking mid+1
        check = mid+1;

        if(right > mid+1 && arr[check] >= arr[check-1] && arr[check] >= arr[check+1]){
            if(right_split == -1 || arr[right_split] > arr[check]){
                right_split = check;
            }
        }

        //compare found solutions from above
        if(left_split == -1){
            smallest = right_split;
        } else if(right_split == -1){
            smallest = left_split;
        } else{
            if(arr[left_split] < arr[right_split]){
                smallest = left_split;
            } else { smallest = right_split; }
        } 
    }

    //check corner cases

    if(right-left+1 == n){
        if(arr[left] >= arr[left+1]){
            if(smallest == -1 || arr[left] < arr[smallest]){
                smallest = left;
            }
        }
        if(arr[right] >= arr[right-1]){
            if(smallest == -1 || arr[right] < arr[smallest]){
                smallest = right;
            }
        }
    }

    //printf("%d", smallest);
    return smallest;
}

int main(){
    int arr[] = {7, 19, 6, 4, 8, 2, 5, 10};
    int n = 8;

    int result = apex(arr, n, 0, 7);
    printf("The smallest apex in the given array is at index %d\n", result);
}