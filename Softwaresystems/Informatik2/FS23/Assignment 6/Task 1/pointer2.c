#include <stdio.h>
#include <stdlib.h>

int main(){
    int a = 1;
    int *p;
    p = malloc(sizeof(int));
    *p = 2;
    a = *p;

    free(p);

    printf("%d", a);

    return 0;
}