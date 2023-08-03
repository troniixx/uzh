#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <limits.h>



int coinRec(int amount, int d[], int m){
    if(amount <= 0){ return 0; }

    int coins = INT_MAX;

    for(int k = 0; k < m; k++){
        if(d[k] <= amount){ 
            int nr = coinRec(amount-d[k], d, m); 
            if(nr != INT_MAX && nr+1 < coins){
                coins = nr + 1;
                }    
            }   
    }

    return coins;
}

int coinMemo(int amount, int d[], int m, int memo[]){
    if(memo[amount] != -1){return memo[amount];}

    int coins = INT_MAX;
    for(int i = 0; i < m; i++){
        if(d[i] <= amount){
            int nr = coinMemo(amount-d[i], d, m, memo);
            if(nr != INT_MAX && nr + 1 < coins){
                coins = nr + 1;
            }
        }
    }

    memo[amount] = coins;
    return coins;
}

int coinDP(int amount, int d[], int m){
    int dp[20];
    for(int i = 0; i < 20; i++){ dp[i] = INT_MAX; }
    dp[0] = 0;

    for(int i = 1; i <= amount; i++){
        for(int j = 0; j < m; j++){ 
            if(d[j] <= i){
                int nr = dp[i-d[j]];
                if(nr != INT_MAX && nr + 1 < dp[i]){
                    dp[i] = nr + 1;
                }
            }
        }   
    }

    if(dp[amount] == INT_MAX){
        return -1;
    }

    return dp[amount];
}

int main(){
    int m = 3; //length of d
    int d[] = {2, 5, 6};
    int memo[20];

    printf("Recursive:\nThe number of coins needded is: %d\n", coinRec(9, d, m));

    for(int i = 0; i < 20; i++){ memo[i] = -1; }
    memo[0] = 0;
    printf("Memoization:\nThe number of coins needded is: %d\n", coinMemo(9, d, m, memo));
    printf("DP:\nThe number of coins needded is: %d\n", coinDP(9, d, m));
}