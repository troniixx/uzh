#include <stdio.h>
#include <stdlib.h>

int main(){
    int a[3] = {1, 2, 3};
    int *p;

    //p = a; p++;

    //p = &a[0]; p++;

    int b[3] = a; // this is the invalid one, you cant put a list into a list

    //int b = *(a+1);

    return 0;
}