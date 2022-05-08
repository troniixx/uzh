#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#define SIZE 20

struct Item {
    int data;
    int key;
};

struct Item* HashArray[SIZE];
struct Item* blank;
struct Item* item;

int Encoding(int key){
    return key%SIZE;
}

struct Item *search(int key){ 
    int hashIndex = Encoding(key);

    while(HashArray[hashIndex] != NULL){

        if(HashArray[hashIndex]->key == key){
            return HashArray[hashIndex];
        }
        ++hashIndex;

        hashIndex %= SIZE;
    }

    return NULL;
}


struct Item *insert(int key, int data){

    struct Item *item = (struct Item*)malloc(sizeof(struct Item));
    item->data = data;
    item->key = key;

    int hashIndex = Encoding(key);

    while(HashArray[hashIndex] != NULL && HashArray[hashIndex]->key != -1){
        ++hashIndex;
        hashIndex %= SIZE;
    }

    HashArray[hashIndex] = item;
}

struct Item* delete(struct DataItem* item) {
    int key = item->key;

    int hashIndex = Encoding(key);
    
    while(HashArray[hashIndex] != NULL){
        if(HashArray[hashIndex]->key == key){
            struct Item* temp = HashArray[hashIndex];

            HashArray[hashIndex] = blank;
            return temp;
        }

    ++hashIndex;
    hashIndex %= SIZE;
    }

    return NULL;
}

void display() {
    int i = 0;
	
    for(i = 0; i<SIZE; i++) {
	
        if(hashArray[i] != NULL)
            printf(" (%d,%d)",HashArray[i]->key,HashArray[i]->data);
        else
            printf(" ~~ ");
        }
	
    printf("\n");
}

void main(){
    
}