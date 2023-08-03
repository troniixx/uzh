#include <stdio.h>

int a, b, c, d, i, j;

// row >
// column ^

// i did this inside the main function at first but 
// it looks cleaner and more professional this way :)
// l = length of row of matrice, r = row of matrice
void printer(int l, int r[]) {
    int i = 0;
    for (i = 0; i < l; i++) {
        printf("%d\t", r[i]);
    }
}

int main()
{

    printf("Enter four integers to fill the matrice:\n");
    int input = scanf("%i %i %i %i", &a, &b, &c, &d);

    int original[2][2] = {{a, b},
                        {c, d}};

    int squared[2][2] = {{a*a+c*b, a*b+d*b},
                        {a*c+c*d, b*c+d*d}};

    printf("\n");
    printf("Printing the matrices:\n\n");

    for (j = 0; j < 2; j++) {
        printer(2, original[j]);
        printf("\t");
        printer(2, squared[j]);
        printf("\t\n");
    }

    return 0;
}
