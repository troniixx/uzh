#include <stdio.h>
#define n 5

int j, q;
int a[] = {11, 1, 4, -3, 22};

int main(){
    j = 0;
    q = -3;

    while(j<n && a[j] != q) {
        j++;
    }

    if(j<n) {
        printf("%d\n", j);
    } else {
        printf("NIL\n");
    }
}

// Solution: it returns NIL
// The while loop iterates through the list a
// When j is equal or larger to n and a[j] is equal q
// the loop ends and moves to the if block
// because j isn't smaller than n it moves to the else block
// and returns NIL