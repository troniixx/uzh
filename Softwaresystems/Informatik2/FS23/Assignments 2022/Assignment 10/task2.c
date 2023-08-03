#include <stdio.h>
#include <stdlib.h>

#define m 7

struct HTElement {
    int val;
    int status; // -2; Deleted -1; Empty 0; Occupied
};

void init(struct HTElement arr[]){
    for(int i = 0; i < m; i++){
        arr[i].val = 0;
        arr[i].status = -1;
    }
}

int hash(int k, int i){
    int one = (k%m)+1;
    int two = (m-1)-(k%(m-1));
    int done = (one + i*two) % m;

    return done;
}

void insert(struct HTElement arr[], int key){
    int counter = 0;
    int hkey;

    while(arr[hkey].status == 0 && counter++ < m){
        hkey = hash(key, counter);
    }

    arr[hkey].status = 0;
    arr[hkey].value = key;
}

void delete(struct HTElement arr[], int key){

}

int search(struct HTElement arr[], int key){

}

void printHashTable(struct HTElement arr[]){
    for(int i = 0; i < m; i++){
        if (arr[i].status == 0){
            printf("i: %d\tkey: %d\n", i, arr[i].value);
        }
    }
}

int main() {
    struct HTElement arr[m];
    init(arr);

    insert(arr, 1313);
    insert(arr, 1314);
    insert(arr, 1315);
    insert(arr, 2000);
    insert(arr, 2001);
    insert(arr, 2002);

    printHashTable(arr);

    int searchValues[] = {2000, 10, 1314, 1313, 337};
    int i;
    for (i = 0; i < 5; i++) {
        if (search(arr, searchValues[i]) == -1) {
        printf("Searching for %d, not found\n", searchValues[i]);
        }
        else {
        printf("Searching for %d, found %d\n", searchValues[i], search(arr, searchValues[i]));
        }
    }
    printf("deleting 1313\n");
    delete(arr, 1313);
    printHashTable(arr);

    printf("re-inserting 1313\n");
    insert(arr, 1313);
    printHashTable(arr);
    
    printf("deleting 1313 again\n");
    delete(arr, 1313);
    printHashTable(arr);

    for (i = 0; i < 5; i++) {
        if (search(arr, searchValues[i]) == -1) {
        printf("Searching for %d, not found\n", searchValues[i]);
        }
    else {
        printf("Searching for %d, found %d\n", searchValues[i], search(arr, searchValues[i]));
        }
    }
}   
