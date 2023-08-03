#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

int given[4][6] = { {1, 7, 3, 2, 6, 1},
                    {2, 5, 4, 5, 9, 3}, 
                    {6, 3, 2, 6, 6, 6},
                    {8, 7, 5, 4, 8, 7}
                    };

int longestPath(int x, int y, int m[x][y]); int max3(int a, int b, int c); int max2(int a, int b);

int main(){

    printf("The longest path is of length: %d\n", longestPath(4, 6, given));
    return 0;
}


int longestPath(int x, int y, int m[x][y]){
    int s[x][y];

    for(int i = 0; i < x; i++){ 
        for(int j = 0; j < y; j++){
            s[i][j] = INT_MAX;
        }
    }

    int max = 0;
    int new = 0;

    for(int i = 0; i < x; i++){
        for(int j = 0; j < y; j++){
            if(j - 1 >= 0 && i - 1 >= 0 && abs(m[i][j] - m[i][j - 1]) && abs(m[i][j]-m[i-1][j]) <= 1){
                new = max3(1, s[i][j-1]+1, s[i-1][j]+1);
                s[i][j] = new;
                if(new > max){
                    max = new;
                }
            } else if(j - 1 >= 0 && abs(m[i][j]-m[i][j-1]) <= 1){
                new = max2(1, s[i][j-1]+1);
                s[i][j] = new;
                if(new > max){
                    max = new;
                }
            } else if(i - 1 >= 0 && abs(m[i][j]-m[i-1][j]) <= 1){
                new = max2(1, s[i-1][j]+1);
                s[i][j] = new;
                if(new > max){
                    max = new;
            }
        } else {
            s[i][j] = 1;
        }
    }
    }
    return max;
}

int max3(int a, int b, int c) {
    int max = a;

    if (b > max) {
        max = b;
    }

    if (c > max) {
        max = c;
    }

    return max;
}

int max2(int a, int b){
    if(a < b) return b;

    return a;
}
