#include <stdio.h>
/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/

int max_of_four(int a, int b, int c, int d){
    int maxi;
    
    if(a > b && a > b && a > c && a > d){
        return a;
    } else if (b > a && b > c && b > d){
        return b;
    } else if (c > a && c > b && c > b) {
        return c;
    }
    else{
        return d;
    }
    
    return maxi;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}