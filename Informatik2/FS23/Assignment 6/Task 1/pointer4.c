#include <stdio.h>
#include <stdlib.h>

void swap1(int a, int b){
    int temp;

    temp = a;
    a = b;
    b = temp;
}

void swap2(int *a, int *b){
    int temp;
    
    temp = *a;
    *a = *b;
    *b = temp;
}

int main(){
    int a = 1;
    int b = 2;
    swap1(a, b);
    printf("%d, %d, ", a, b);

    swap2(&a, &b);
    printf("%d, %d, ", a, b);

    return 0;
}