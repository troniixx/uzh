#include <stdio.h>

int whatDoesItDo(int arr[], int n, int k){
    int result = -1000;

    for(int i = 1; i < n; i++){
        int current = 0;
        for(int j = i; j < n; j = j+k){
            current = current + arr[j];
    }
        if(current > result) {
            result = current;
        }
    return result;
    }
}

int main() {
    int arr[] = {1,3,5,4,2,6,8};
    int n = 7;
    int k = 3;

    printf("The output for this example is: %d", whatDoesItDo(arr, n, k));
    return 0;
}