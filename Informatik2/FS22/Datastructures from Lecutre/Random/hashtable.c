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

    return NULL;
}

struct Item* delete(struct Item* item) {
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
	
        if(HashArray[i] != NULL)
            printf(" (%d,%d)",HashArray[i]->key,HashArray[i]->data);
        else
            printf(" ~~ ");
        }
	
    printf("\n");
}

int main() {
    blank = (struct Item*) malloc(sizeof(struct Item));
    blank->data = -1;  
    blank->key = -1; 

    insert(1, 20);
    insert(2, 70);
    insert(42, 80);
    insert(4, 25);
    insert(12, 44);
    insert(14, 32);
    insert(17, 11);
    insert(13, 78);
    insert(37, 97);

    display();
    item = search(37);

    if(item != NULL) {
        printf("Element found: %d\n", item->data);
    } else {
        printf("Element not found\n");
    }

    delete(item);
    item = search(37);

    if(item != NULL) {
        printf("Element found: %d\n", item->data);
    } else {
        printf("Element not found\n");
    }

    return 0;
}