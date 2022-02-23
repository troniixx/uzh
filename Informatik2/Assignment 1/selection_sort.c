#include <string.h>
#include <stdio.h>

int even_odd_selection(int A[], int n) {

    int i, j;
    int arr[50]; /*even*/
    int arr1[50]; /*odd*/
    
    /* split array into even and odd */
    for(i = 0; i <= n; ++i) {
        if(A[i] % 2 == 0){
            arr[i] = A[i];
        } else {arr1[i] = A[i];}
    }

}


int main() {
    return 0;
}