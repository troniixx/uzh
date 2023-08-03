#import <stdio.h>
#import <stdlib.h>


int i, j, k, n;
int A[8], B[8], l, r, m;
void mergeSort(int A[], int l, int r); void merge(int A[], int l, int m, int r); void printArray(int A[], int n);

int main(){

    int A[] = {12, 11, 31, 5, 2, 7, 1};
    n = 7;

    printf("Given Array: \n");
    printArray(A,  n);

    mergeSort(A, 0, n-1);

    printf("Sorted Array: \n");
    printArray(A, n);


    return 0;
}

//Just simple function to print arrays
void printArray(int A[], int n){

    for(i = 0; i < n; i++){
        printf("%d ", A[i]);
    }
    printf("\n");
}

void mergeSort(int A[], int l, int r){
    if(l < r){
        m = l + (r - l)/2;

        mergeSort(A, l, m); //Mergesort the left part
        mergeSort(A, m+1, r); //Mergesort the right part
        merge(A, l, m, r); //Merge both parts above togehter
    }
}

void merge(int A[], int l, int m, int r){

    //size of temp arrays
    int n1 = m-l+1 ;
    int n2 = r-m;

    //define temp arrays to use to mergesort
    int Left[n1], Right[n2];

    //copy into temp arrays
    for(int i = 0; i < n1; i++){
        Left[i] = A[l+i];
    }
    for(int j = 0; j < n2; j++){
        Right[j] = A[m+1+j];
    }

    //Merge temp arrays back into original
    i = 0; j = 0; k = l;

    while(i < n1 && j < n2){
        if(Left[i] <= Right[j]){
            A[k] = Left[i];
            i++;
    } else {
        A[k] = Right[j];
        j++;
    }
    k++;
    }

    // Copy remaining items of Left and Right side temp arrays
    while(i < n1){
        A[k] = Left[i];
        i++;
        k++;
    }
    while(j < n2){
        A[k] = Right[j];
        j++;
        k++;
    }
}
