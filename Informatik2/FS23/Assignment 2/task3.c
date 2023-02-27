#include <stdio.h>

void hanoi(int d, int a, int b, int c){

        if(d == 1){
            printf("Move from rod %i to rod %i\n", a, c);
            return;
        }
        hanoi(d-1, 1, 2, 3);
        printf("Move from rod %i to rod %i\n", a, c);
        hanoi(d-1, 2, 3, 1);


}

int main(){

    int disks;
    printf("Enter # of Disks: ");
    scanf("%d", &disks);
    hanoi(disks, 1, 2, 3);
    return 0;
}