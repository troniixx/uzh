#include <stdio.h>
#include <string.h>

int i, j, m, n, DP_Table[20][20];
char S1[20] = "ACADB", S2[20] = "CBDA", b[20][20];

void lcsAlgo(){

    m = strlen(S1);
    n = strlen(S2);

    //filling matrix with 0
    for(i = 0; i <= m; i++){
        DP_Table[i][0] = 0;
    }
    for(i = 0; i <= n; i++){
        DP_Table[0][i] = 0;
    }

    //bottom up approach -  dont get mad at me for not doing the others
    for(i = 1; i <= m; i++){
        for(j = 1; j <= n; j++){
            if(S1[i-1] == S2[j-1]){
                DP_Table[i][j] = DP_Table[i][j-1]+1;
            } else if(DP_Table[i-1][j] >= DP_Table[i][j-1]) {
                DP_Table[i][j] = DP_Table[i-1][j];
            } else {
                DP_Table[i][j] = DP_Table[i][j-1];
            }
        }
    }

    int idx = DP_Table[m][n];
    char lcs[idx+1];
    lcs[idx] = '\0';

    int i = m, j = n;
    while(i > 0 && j > 0){
        if(S1[i - 1] == S2[j - 1]){
            lcs[idx - 1] = S1[i - 1];
            i--;
            j--;
            idx--;
        } else if (DP_Table[i - 1][j] > DP_Table[i][j-1]){
            i--;
        } else {
            j--;
        }
        }

    //print the lcs
    printf("S1: %s \nS2: %s \n", S1, S2);
    printf("LCS: %s", lcs);

    }

int main(){
    lcsAlgo();
    printf("\n");
    return 0;
}