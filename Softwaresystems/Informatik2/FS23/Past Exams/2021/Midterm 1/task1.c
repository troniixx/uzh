#include <stdio.h>
#include <stdlib.h>

int d(int i){
    int sum = i;

    while(i != 0){
        sum = sum + (i%10);
        i = i/10;
    }

    return sum;
}

void DNumbers(int i, int n){
    for(int j = 1; j <= n; j++){
        i = d(i);
        printf("%d\n",i);
    }
}

int main(){
    DNumbers(81,4);
}