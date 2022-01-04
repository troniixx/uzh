#include <stdio.h>

void swap(int *xp, int *yp) {

    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

