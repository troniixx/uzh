#include <string.h>
#include <stdio.h>
#include <stdbool.h>

bool is_vowel(int A[]) {
    int i;
    int n = sizeof(A);

    for(i = 0; i < n; ++i) {
        if(A[i] == 'a' || A[i] == 'e' || A[i] == 'i' || A[i] == 'o' || A[i] == 'u' || 
        A[i] == 'A' || A[i] == 'E' || A[i] == 'I'|| A[i] == 'O' || A[i] ==  'U') {
            return true;
        } else {return false;}
    }
}

char print_array(char A[]) {
    int n = sizeof(A);

    for (int i = 0; i < n; ++i){
        printf("%s", A[i]);
    }
}

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
    int counter = count_vowels(A);
    int len_arr = sizeof(A);
    int len = sizeof(A) + 2*counter;
    char sol[len+1];
    int pos = 0;
    
    for(int i = 1; i < len_arr; ++i) {
        if(is_vowel(A[i])){
            sol[pos] = A[i];
            sol[pos+1] = 'b';
            sol[pos+2] = A[i];
            pos = pos+3;
        } else {
            sol[pos] = A[i];
            pos = pos+1;
        }
    }

    print_array(sol);
}

int main() {

    int num;
    char A[] = "Hello Worldi";

    num = count_vowels(A);
    printf("The number of vowels in the given string is: %d", num);

}