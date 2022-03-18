#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool is_balanced_iterative(int A[], int l, int r){

    int m = floor((l+r)/2);
    int size = sizeof(*A)/sizeof(A[0]);
    int sum1 = 0;
    int sum2 = 0;

    if(size == 1){ return true;
    } else {
        for(int i = 0; i <= m; i++){
            sum1 = A[i] + sum1;
        }

        for(m+1; m < size; m++ ){
            sum2 = A[m] + sum2;
        }

        if((sum1 <= sum2*2) && (sum1 >= sum2/2)){ return true; } else { return false; }

    }

}

int main(){
    int arr[] = {1,3,10,2,3,7,5,7};
    printf("If 1 gets returned then the array is balanced: %i\n", is_balanced_iterative(arr, arr[0], arr[8]));
}