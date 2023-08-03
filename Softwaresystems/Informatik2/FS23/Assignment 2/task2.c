#include <stdio.h>

void printRec(int n){
    
    if(n == 0){
        return;
    }

    if(n == 1){
        printf("0");
        return;
    }

    printf("%d", n%2);

    printRec(n/1.75);
}

int main(){
    printRec(20);
    return 0;
}
