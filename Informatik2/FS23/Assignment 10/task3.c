#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define m 7
int u;

void init(int arr[]); int h(int k, int i); void insert(int arr[], int key); int search(int arr[], int key); void printHash(int arr[]);

int main(){
    int HT[m];

    printf("Indexing starts at 0!\n"); printf("\n");
    init(HT);
    insert(HT, 1313); insert(HT, 1314); insert(HT, 1315); insert(HT, 2000); insert(HT, 2001); insert(HT, 2002);
    printf("Hashtable after inserting: \n");
    printHash(HT); printf("\n");
    printf("\n");


    printf("This part shows the results for the search function: \n");
    printf("Seach for 2000: "); printf("It is at index %d", search(HT, 2000)); printf("\n");
    printf("Seach for 10: "); printf("It is at index %d", search(HT, 10)); printf("\n");
    printf("Seach for 1314: "); printf("It is at index %d", search(HT, 1314)); printf("\n");
    printf("Seach for 1313: "); printf("It is at index %d", search(HT, 1313)); printf("\n");
    printf("Seach for 337: "); printf("It is at index %d", search(HT, 337)); printf("\n");

    return 0;
}

void init(int arr[]){
    for(int j = 0; j < m; j++){
        arr[j] = 0;
    }
}

int h(int k, int i){
    int m_dash = m - 1;
    int h_one = (k % m)+1;
    int h_two = m_dash - (k % m_dash);
    
    int h = (h_one + (i * h_two)) % m;

    return h;
}

void insert(int arr[], int key){
    int hash = h(key, u);

    if(arr[hash] == 0){
        arr[hash] = key;
    } else {
        u = u+1; 
        insert(arr, key);
        }
}


int search(int arr[], int key){
    
    for(int i = 0; i < m; i++){
        if(arr[i] == key){
            return i;
            }
        }
    return -1;
}

void printHash(int arr[]){
    for(int i = 0; i < m; i++){
        if(arr[i] != 0){
        printf("%d - %d\n", i, arr[i]);
            }
    }
}