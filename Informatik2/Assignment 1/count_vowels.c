#include <string.h>
#include <stdio.h>

int count_vowels(char A[]) {

    int i, n, count;
    n = strlen(A);
    count = 0;

    for(i = 0; i <= n; i++){
        if(A[i] == 'a' || A[i] == 'e' || A[i] == 'i' || A[i] == 'o' || A[i] == 'u' || 
        A[i] == 'A' || A[i] == 'E' || A[i] == 'I'|| A[i] == 'O' || A[i] ==  'U') {
            count++;
        }
    }

    return count;

}

void BS(char A[]){
    return;
}

int main() {

    int num;
    char A[] = "Hello Worldi";

    num = count_vowels(A);
    printf("The number of vowels in the given string is: %d", num);

}