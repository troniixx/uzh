#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int a(int n){
    int i;
    for(i = 1; i < n; i++){
        if(i*(i+1) == n){
            printf("True\n");
            return 1;
        }
    }
    printf("False\n");
    return 0;
}

int b(int n){
    int i;
    for(i = 1; i*i < n; i++){
        if(i*(i+1) == n){
            printf("True\n");
            return 1;
        }
    }
    printf("False\n");
    return 0;
}

int main(){
    clock_t start, end;

    start = clock();
    a(25000);
    end = clock();
    double runtime = ((double)(end-start))/(CLOCKS_PER_SEC/1000);
    printf("Given version takes: %f ms\n", runtime);

    start = clock();
    b(25000);
    end = clock();
    runtime = ((double)(end-start))/(CLOCKS_PER_SEC/1000);
    printf("Improved version takes: %f ms\n", runtime);
}