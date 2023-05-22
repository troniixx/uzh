#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int given[6][6] = {{0, 0, 0, 1, 0, 0},
                    {0, 1, 0, 1, 0, 0},
                    {1, 1, 1, 1, 1, 1},
                    {1, 1, 0, 1, 0, 1},
                    {1, 0, 0, 1, 1, 0}
                    };

void makeHelper(int x, int y, int m[x][y], int top[x][y], int bottom[x][y], int left[x][y], int right[x][y]);
int biggestPlus(int x, int y, int m[x][y]); int min4(int a, int b, int c, int d);

int main(){
    printf("The biggest plus is of size: %d\n", biggestPlus(6, 6, given));

    return 0;
}

void makeHelper(int x, int y, int m[x][y], int top[x][y], int bottom[x][y], int left[x][y], int right[x][y]){
    for(int i = 0; i < x; i++){
        for(int j = 0; j < y; j++){
            if(m[i][j] == 1){
                if(i - 1 >= 0){
                    top[i][j] = top[i - 1][j] + 1;
                } else {
                    top[i][j] = 1;
                }
                if(j - 1 >= 0){
                    left[i][j] = left[i][j-1] + 1;}
                else {
                    left[i][j] = 1;} 
            }
        else{
            top[i][j] = 0;
            left[i][j] = 0;
            }
        }
    }

    for(int i = x - 1; i >= 0; i--){
        for(int j = y - 1; j >= 0; j--){
            if(m[i][j] == 1){
                if(i + 1 < x){
                    bottom[i][j] = bottom[i + 1][j] + 1;
                }
                else {
                    bottom[i][j] = 1;
                }
            if(j + 1 < y){
                right[i][j] = right[i][j + 1] + 1;
            } else {
                right[i][j] = 1;
                }
            }
            else{
                bottom[i][j] = 0;
                right[i][j] = 0;
            }
        }
    }
}

int biggestPlus(int x, int y, int m[x][y]){
    int bottom[x][y]; int left[x][y]; int right[x][y]; int top[x][y];
    makeHelper(x, y, m, bottom, left, right, top);

    int max = 0; int new; int s[x][y];

    for(int i = 0; i < x; i++){
        for(int j = 0; j < y; j++){
            new = min4(bottom[i][j], top[i][j], left[i][j], right[i][j]);
            if(new < 1){
                new = 0;
            } else {
                new = (new - 1)*4 + 1;
            }
            s[i][j] = new;
            if(new > max){
                max = new;
            }
        }
    }

    return max;
}

int min4(int a, int b, int c, int d) {
    int min = a; 

    if (b < min) {
        min = b;
    }

    if (c < min) {
        min = c;
    }

    if (d < min) {
        min = d;
    }

    return min;
}