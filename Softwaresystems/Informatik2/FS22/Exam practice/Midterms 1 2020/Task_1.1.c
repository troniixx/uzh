#include <stdio.h>

int sum(int A[], int B[], int n){
    int x;
    int a = 0;
    int b = 0;
    int total = 0;


    for (x = 0; x < n; x++)
        a = (a * 10) + A[x];
        
    for (x = 0; x < n; x++)
        b = (b * 10) + B[x];
        
    total = a+b;
    
    return total;
}

int main()
{
    int A[] = {1, 2, 3};
    int B[] = {3, 2, 1};
    
    int n = sizeof A / sizeof A[0];
    
    int sol = sum(A, B, n);
    printf("The sum of the two arrays is: %d", sol);

    return 0;
}
