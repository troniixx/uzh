#include <stdio.h>
#include <time.h> // measuring run time

/*
Solutions 1c)

linear_search = O(n)
binary_search = O(logn)

Solutiuons 1d)

n = 1000000, t = 1000000 --> lin. search = 2.963 ms // bin. search 0.003ms
n = 10000000, t = 10000000 --> lin. search = 27.05 ms // bin. search 0.002 ms
n = 100000000, t = 100000000 --> lin. search = 272.377 ms // bin. search 0.002 ms

*/

int n, t;
int A[100000000];

int linear_search(int A[], int n, int t) {
    // 1a) write your code
    for(int i = 0; i < n; i++){
        if(A[i] == t){
            return 1;
        }
    }

    return 0; // not found
}

int binary_search(int A[], int n, int t) {
    // 1b) write your code
    int l = 0;
    int r = n;
    int m = (l+r)/2;

    while(l < r && t != A[m]){
        if(t < A[m]){
            r = m-1;
        } else {
            l = m+1;
        }

        m = (l+r)/2;
    }

    if(l <= r){
        return 1;
    }

    
    return 0; // not found
}

int main() {
    clock_t start, end;
    printf("Enter an integer for n: ");
    scanf("%d", &n); 
    printf("Generate an array with %d distinct integers from 1 to %d.\n", n, n);
    for(int i = 0; i < n; i++) A[i] = i + 1;
    printf("Enter an integer for t: \n");
    scanf("%d", &t); 
    start = clock();
    linear_search(A, n, t); // your implementation
    end = clock();
    double run_time = ((double)(end - start))/(CLOCKS_PER_SEC/1000);
    printf("Linear search takes : %f millseconds\n", run_time); 

    start = clock();
    binary_search(A, n, t); // your implementation
    end = clock();
    run_time = ((double)(end - start))/(CLOCKS_PER_SEC/1000);
    printf("Binary search takes : %f millseconds\n", run_time); 
}