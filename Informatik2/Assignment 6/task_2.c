#include <stdio.h>
#include <math.h>
#include <stddef.h>

struct Node{
    int data;
    struct Node* next;
};

struct Node *head, *temp, *new;

void displayList(){
    temp = head;

    while(temp != 0){
        printf("%d, ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

void insertList_beginning(int value){
    new = (struct Node *)malloc(sizeof(struct Node));
    new->data = value;
    new->next = head;
    head = new;
}

void insertList_end(int value){
    if (head == NULL){ 
        head = (struct Node *)malloc(sizeof(struct Node));
        head->data = value;
        head->next = NULL;
    } else { 

        temp = head;
        while(temp->next != NULL){temp = temp->next;}

        temp->next = (struct Node *)malloc(sizeof(struct Node));
        temp->next->data = value;
        temp->next->next = NULL;
    }
}

void groupingLinkedList(){

}

int main() {

}