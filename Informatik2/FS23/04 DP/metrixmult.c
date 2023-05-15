#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

int minNumberMult_rec(int arr[], int i, int j){
    if(i == j){ return 0;}
    int k;
    int min = INT_MAX;
    int count;

    for(k = i; k < j; k++){
        count = minNumberMult_rec(arr, i, k) + minNumberMult_rec(arr, k+1, j) + arr[i-1] * arr[k] * arr[j];
        if(count < min){ min = count; }
    }

    return min;
}

int minNumberMult_dp(int arr[], int n){
    int dp[n][n];
    int i, j, k, l, q;

    for(i = 1; i < n; i++){
        dp[i][i] = 0;
    }

    for(l = 2; l < n; l++){
        for(i = l; i < n-l+1; i++){
            j = i+l-1;
            dp[i][j] = INT_MAX;

            for(k = i; k <= j-1; k++){
                q = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j];
                if(q < dp[i][j]){
                    dp[i][j] = q;
                }
            }
        }
    }

    return dp[1][n-1];
} 

int main(){

    int arr[] = {1, 2, 3, 4};
    int n = sizeof(arr)/sizeof(arr[0]);

    printf("Recursive:\n");
    printf("Minimum Number of Multiplications: %d\n", minNumberMult_rec(arr, 1, n-1));
    printf("Dynamic Programming:\n");
    printf("Minimum Number of Multiplications: %d\n", minNumberMult_dp(arr, n));
}