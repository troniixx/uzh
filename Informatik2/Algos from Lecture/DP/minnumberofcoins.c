#include <stdio.h>
#include <limits.h>

// k = value to change, n = length of d, d = array of availiable coins
int coin_change(int d[], int n, int k)
{
    if(k == 0) {return 0; }

    int Change[k+1];
    Change[0] = 0;

    //init the array
    for(int i = 1; i <= k; i++){ Change[i] = INT_MAX;}

    //solving in bottom up approach
    for(int i = 1; i <= k; i++){
        for(int j = 0; j <= n; j++){
            if(d[j] <= i){
                int curr = Change[i - d[j]];
                if(curr != INT_MAX && curr+1 < Change[i]){ Change[i] = curr+1; }
            }
        }
    }
    
    //returns min amount if possible or -1 if not possible
    if(Change[k] == INT_MAX){ return -1; }
    else { return Change[k]; }
}

int main()
{   
    int d[] = {25, 10, 5};
    int k = 30;
    int n = sizeof(d)/sizeof(d[0]);
    int sol = coin_change(d, n, k);

    printf("The minimum number of required coins is: %d\n", sol);
}