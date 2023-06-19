#include <stdio.h>
#include <stdlib.h>

int d(int i){
    int sum = i;
    while(i != 0){
        sum = sum + i%10;
        i = i/10;
    }
    return sum;
}

void DNumbers(int i, int n){
    int k;

    for(k = 1; k <= n; k++){
        i = d(i);
        printf("%d ", i);
    }
    printf("\n");

}

int main(){
    DNumbers(81, 4);
}