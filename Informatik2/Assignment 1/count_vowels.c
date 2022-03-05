#include <string.h>
#include <stdio.h>

int is_vowel(char letter) {
    
    if(letter == 'A' || letter == 'E' || letter == 'I' || letter =='O' || letter == 'U' ||
        letter == 'a' || letter == 'e' || letter == 'i' || letter =='o' || letter == 'u') {

            return 1;

        } else {return 0;}
    }


int count_vowels(char A[]) {

    int count_vowels = 0;
    int pos = 0;

    while (A[pos] != '\0') {
        if (is_vowel(A[pos])) {
            count_vowels++;
        }
        pos++;
    }

    return count_vowels;
}

void BS(char A[]){
    int pos_in = 0;
    int pos_sol = 0;
    int count_v = count_vowels(A);
    int n = (sizeof(*A) / sizeof(A[0]));
    const int new_len = n + 2 * count_v;
    char sol[new_len + 1];
    
    while (A[pos_in] != '\0') {
        if (is_vowel(A[pos_in])) {
            sol[pos_sol] = A[pos_sol];
            sol[pos_sol + 1] = 'b';
            sol[pos_sol + 2] = A[pos_in];
            pos_sol = pos_sol + 3;
    }
        else {
            sol[pos_sol] = A[pos_in];
            pos_sol = pos_sol + 1;
        }
        pos_in++;
    }

    sol[new_len] = '\0';
    printf("B-Sprache: %s\n", sol);
}

int main() {

    int num;
    char A[] = "Informatik";
    BS(A);

    num = count_vowels(A);

    printf("The number of vowels in the given string is: %d", num);

}