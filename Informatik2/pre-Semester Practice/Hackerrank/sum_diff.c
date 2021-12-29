#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int a;
    int b;
    float c;
    float d;

    scanf("%d %d", &a, &b);
    scanf("%f %f", &c, &d);
    
    printf("%d %d", a+b, a-b);
    printf("\n");
    printf("%.1f %.1f", c+d, c-d);
    
    return 0;
}