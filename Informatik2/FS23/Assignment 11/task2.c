#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>
#include <string.h>

int isPalindrome(char x[], int i, int j); int findMinCutsRecursive(char x[], int i, int j); int findMinCutsDP(char x[], int n);

int main(){
    char x[] = "ABA";
    int j = strlen(x);

    printf("Is palindrome: %d", isPalindrome(x, 0, j));
    //printf("Recursive (Should equal to 2): %d\n", findMinCutsRecursive(x, 0, 5));
    //printf("Dynamic Programming (Should equal to 2): %d\n", findMinCutsDP(x, n));
}

int isPalindrome(char x[], int i, int j){
    j = j-1;

    if(NULL == x || i < 0 || j < 0){
        return 0;
    }
    if(i >= j){
        return 1;
    }
    if(x[i] == x[j]){
        return isPalindrome(x, i + 1, j - 1);
    }
    return 0;
}

