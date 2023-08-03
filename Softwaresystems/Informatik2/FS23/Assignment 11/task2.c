#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>
#include <string.h>

int isPalindrome(char x[], int i, int j); int findMinCutsRecursive(char x[], int i, int j); int findMinCutsDP(char x[], int n);
int min(int a, int b);

int main(){
    char x[] = "ABBCDC";
    printf("Palindrome?: %d\n", isPalindrome(x, 0, 5));
    printf("Recursive: %d\n", findMinCutsRecursive(x, 0, 5));
    printf("Dynamic: %d\n", findMinCutsDP(x, 6)); 
}

int min(int a, int b){
    if(a < b){ return a;}

    return b;
}

int isPalindrome(char x[], int i, int j){
    while(i <= j){
        if(x[i] != x[j]){
            return 0;
        }
    i++;
    j--;
    }

    return 1;
}

int findMinCutsRecursive(char x[], int i, int j){
    int count = INT_MAX;
    int min = INT_MAX;

    if(i == j || isPalindrome(x, i, j) == 1){
        return 0;
    }

    for(int k = i; k < j; k++){
        count = 1 + findMinCutsRecursive(x, i, k) + findMinCutsRecursive(x, k+1, j);
        if(count < min){ min = count; }
    }

    return min;
}

int findMinCutsDP(char x[], int n){

    int helperM[n][n];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            helperM[i][j] = 0;
        }
    }

    for(int i = n-1; i >= 0; i--){
        for(int j = i; j < n; j++){
            if(j == i){
                helperM[i][j] = 1;
            }
            else if(x[i] == x[j]){
                if(j - i == 1){
                    helperM[i][j] = 1;
                }
                else{
                    helperM[i][j] = helperM[i+1][j-1];
                }
            }
            else {
            helperM[i][j] = 0; }
        } 
    }


    int helperA[n];
    for(int i = 0; i < n; i++){
        helperA[i] = INT_MAX;
    }

    for(int i = n - 1; i >= 0; i--){
        if(helperM[i][n-1] == 1){
            helperA[i] = 0;
        } else {
            for(int j = n - 2; j > i - 1; j--){
                if(helperM[i][j] == 1){
                    helperA[i] = min(helperA[i], helperA[j+1] + 1);
                }
            }
        }
    }
    return helperA[0];
}
