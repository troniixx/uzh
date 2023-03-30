#include <stdio.h>
#include <stdlib.h>
#define N 5

void print(int *arr, int n); int* reverse(int *arr, int n); int* prepend(int *arr, int v);

int main(){
    int*arr;
    arr = malloc(N*sizeof(int));

    for(int i = 0; i < N; i++){
        arr[i] = i;
    }

    printf("The original");
    print(arr, N);

    int *reversed = reverse(arr, N);
    free(arr);

    printf("The reversed");
    print(reversed, N);

    int *prepended = prepend(reversed, 5);

    free(reversed);

    printf("The prepend");
    print(prepended, N+1);

    return 0;
}

void print(int *arr, int n){
    for(int i = 0; i < n; i++){
        printf("%d ", *(arr+i));
    }
}

int *reverse(int *arr, int n)
{
    return nullptr;
}

int *prepend(int *arr, int v)
{
    return nullptr;
}
