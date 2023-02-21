#include <stdio.h>

int c = 9;
int i, j;
int temp;


//O(n) runtime
void printer(int A[], int n){
    for(i = 0; i < n; i++){
        printf("%i ", A[i]);
    }
    printf("\n");
}

//O(n^2)
void bubbleSort(int A[], int n){

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (A[j] > A[j + 1]) {
                //checking and swapping adjacent elements when left_elem > right_elem
                int temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
            }
        }
    }
}

void pairSum(int A[], int c, int n){
    for(i = 0; i < n; i++){
        for(j = i + 1; j < n; j++){
            if(A[i] + A[j] == c) {
                printf("%i and %i\n", A[i], A[j]);
            }
        }
    }

    //O(n^2)
}

void pairSumSorted(int A[], int c, int n){
    
    bubbleSort(A, n); //O(n^2)

    //O(n^2)
    for(i = 0; i < n; i++){
        for(j = i + 1; j < n; j++){
            if(A[i] + A[j] == c) {
                printf("%i and %i\n", A[i], A[j]);
            }
        }
    }

    //O(n^2+n^2) = O(n^2)

}

int main(){
    int A[6] = {4, 2, 6, 1, 8, 5};
    int n = sizeof(A)/sizeof(A[0]);

    printf("pairSum:\n");
    pairSum(A, c, n);
    printf("\n\n");
    printf("pairSumSorted:\n");
    pairSumSorted(A, c, n);

    //used to test if sorting works
    //bubbleSort(A, n);
    //printer(A, n);
    }
