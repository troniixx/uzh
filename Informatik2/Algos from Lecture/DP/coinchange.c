#include <stdio.h>

int coins[] = {1,2,3}, sum = 4;
int numOfCoins = 3;

void initDPTable(int DPTable[][sum+1]){
    int i; 

    //first row to 0
    for(i = 1; i <= sum+1; i++){
        DPTable[0][i] = 0;
    }

    //first column to 1
    for(i = 1; i <= sum+1; i++){
        DPTable[i][0] = 1;
    }
}

int solve(int DPTable[][sum+1]){
    int coinIdx, dpSum;

    for(coinIdx = 1; coinIdx < numOfCoins+1; coinIdx++){
        for(dpSum = 1; dpSum < sum+1; dpSum++){
            if(coins[coinIdx-1] > dpSum){
                DPTable[coinIdx][dpSum] = DPTable[coinIdx-1][dpSum];
            } else {
                DPTable[coinIdx][dpSum] = DPTable[coinIdx-1][dpSum] + DPTable[coinIdx][dpSum-coins[coinIdx-1]];
            }
        }
    }

    return DPTable[numOfCoins][sum];

}

int main(){
    int DPTable[numOfCoins+1][sum+1];
    initDPTable(DPTable);
    printf("Total Solutuions: %d", solve(DPTable));
    return 0;
}

