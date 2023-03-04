#include <stdio.h>

void hanoi(int d, int a, int b, int c){
    
    int moves = ;
    //printf("Enter # of Moves: ");
    //scanf("%d", &moves);
    
    while(moves != 0){
        if(d == 1){
            printf("Move from rod %i to rod %i\n", a, c);
            return;
        }
        hanoi(d-1, 1, 2, 3);
        printf("Move from rod %i to rod %i\n", a, c);
        hanoi(d-1, 2, 3, 1);
        moves--; 
        }

    return;

}

int main(){

    int disks, moves;
    printf("Enter # of Disks: ");
    scanf("%d", &disks);
    //printf("Enter # of Moves: ");
    //scanf("%d", &moves);
    hanoi(disks, 1, 2, 3);
    return 0;
}