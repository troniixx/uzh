#include <stdlib.h>
#include <stdio.h>

#define m 5;

struct elem{
    int key;
    int status // 0; occupied, -1; Empty
};

struct elem HT[m];

int hash(int k, int i){
    int h = (k+i)%m;

    return h;
}

int HTInsert(int k){
    for(int i = 0; i < 5; i++){
        if(HT[hash(k, i)] == -1){ HT[hash(k, i)] = k; }
    }
}

int HTDelete(int k){

}

int main(){

}