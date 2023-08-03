#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//int i; int j;
//int c[20][20];


int max(int a, int b){
    if(a > b){
        return a;
    }
    return b;
}

int lcsRec(int m, int n, char *x, char *y){
    if(m == 0 || n == 0){ return 0; }
    else if(x[m] == y[n]){ return lcsRec(m-1, n-1, x, y)+1; }
    else{ return max(lcsRec(m-1, n, x, y), lcsRec(m, n-1, x, y)); }
}

int lcsMemo(int m, int n, char *x, char *y){
    int c[m + 1][n + 1], i, j;
    for(i = 0; i <= m; i++){ c[i][0] = -1; }
    for(j = 0; j <= n; j++){ c[0][j] = -1; }


    if(m == 0 || n == 0){ c[m][n] = 0; return 0;}
    else if(c[m][n] != -1){ return c[m][n]; }
    else if(x[m] == y[n]){ c[m][n] = (lcsMemo(m+1, n+1, x, y)+1); return c[m][n]; }
    else{ return max(lcsMemo(m-1, n, x, y), lcsMemo(m, n-1, x, y)); /*return c[m][n];*/ }
}

int lcsDP(int m, int n, char *x, char *y){
    int c[m + 1][n + 1], i, j;
    for(i = 0; i < m + 1; i++){
        for(j = 0; j < n + 1; j++){
            if(i == 0 || j == 0){
                c[i][j] = 0;
            }else if(x[i - 1] == y[j - 1]){
                c[i][j] = c[i - 1][j- 1] + 1;
            }else{
                c[i][j] = max(c[i -1][j], c[i][j - 1]);
            }    
        }
    }
    return c[m][n];
}

int main(){
    char x[] = "GTATCT";
    char y[] = "GGTTCAT";
    int x_len = strlen(x);
    int y_len = strlen(y);
    int memo[20];

    printf("LCSRec: %d\n", lcsRec(x_len, y_len, x, y));
    printf("LCSMemo: %d\n", lcsMemo(x_len, y_len, x, y));
    printf("LCSDP: %d\n", lcsDP(x_len, y_len, x, y));

}