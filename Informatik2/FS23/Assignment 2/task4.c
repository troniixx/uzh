#include <stdio.h>

void calc(int a[], int l){
    if(l == 0){
        return;
    }
    
    int b[l];
    for(int i = 0; i < l; i++){
        b[i] = a[i] + a[i+1];
    }


    calc(b, l-1);

    for(int z = 0; z < l; z++){
        printf("%d ", a[z]);
    }

    printf("\n");

    
}

int main(){
    int a[5] = {5, 4, 6, 1, 3};

    calc(a, 5);

    return 0;
}