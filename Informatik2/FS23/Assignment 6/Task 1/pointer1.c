#include <stdio.h>
#include <stdlib.h>

int main(){
    int a = 1;
    int *p;
    p = &a;
    printf("%p", p);

    return 0;
}