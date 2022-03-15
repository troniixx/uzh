#include <stdio.h>

void moves(int n, char source, char dest, char intermediate){

    if(n == 1){
        printf("Move disc 1 from %c to %c\n", source, dest);
        return;
    }

    moves(n-1, source, intermediate, dest);
    printf("Move disc %d from %c to %c\n", n, source, intermediate);
    moves(n-1, intermediate, dest, source);
}

int main(){
    int n;

    printf("Enter the number of discs: ");
    scanf("%d", &n);
    printf("The sequence of moves is: \n");
    moves(n, 'A', 'C', 'B');
    return 0;
}