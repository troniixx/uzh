#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#define N 5

void print(int *arr, int n); int* reverse(int *arr, int n); int* prepend(int *arr, int v);

int main(){
    int*arr;
    arr = malloc(N*sizeof(int));

    for(int i = 0; i < N; i++){
        arr[i] = i;
    }

    printf("The original\n");
    print(arr, N);
    printf("\n");

    int *reversed = reverse(arr, N);
    free(arr);

    printf("The reversed\n");
    print(reversed, N);
    printf("\n");

//    int *prepended = prepend(reversed, 5);

    free(reversed);
//
//    printf("The prepend\n");
//    print(prepended, N+1);

    return 0;
}

void print(int *arr, int n){
    for(int i = 0; i < n; i++){
        printf("%d ", *(arr+i));
    }
}

int *reverse(int *arr, int n){
    static int rev[INT_MAX];

    for(int i = n-1; i >= 0; i--){
        rev[n-i-1] = *(arr+i);
    }
    return rev;
}

int *prepend(int *arr, int v){
    
    return nullptr;
}
