#include <stdio.h>
#include <math.h>

int main() {
    double d = 1.2;
    int i = 6;
    char ch = 'a';

    double *p_d;
    int *p_i;
    char *p_ch;

    p_d = &d;
    p_i = &i;
    p_ch = &ch;

    printf("The Values of the variables are %f, %i, %c\n", d, i, ch);
    printf("The Adresses of the variables are: %x, %x, %x\n", p_d, p_i, p_ch);
    printf("The Memory Sizes of the variables are: %zu, %zu, %zu\n", sizeof(d), sizeof(i), sizeof(ch));
}