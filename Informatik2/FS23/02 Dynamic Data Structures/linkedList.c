#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <stdbool.h>


struct node{
    int val;
    struct node* next;
};

//insert at beginnining
void insert_front(struct node** root, int data){

    struct node* new = (struct node*)malloc(sizeof(struct node));
    new->val = data;
    new->next = *root;
    *root = new;
}

//insert after given node prev
void insert_after(struct node* prev, int data){

    if(prev == NULL){
        printf("Previous node can't be null");
        return;
    }

    struct node* new = (struct node*)malloc(sizeof(struct node));
    new->val = data;
    new->next = prev->next;
    prev->next = new;

}

//insert at end
void insert_end(struct node** root, int data){
    struct node* new = (struct node*)malloc(sizeof(struct node));
    struct node* last = *root;

    new->val = data;
    new->next = NULL;

    if(*root == NULL) {
        *root = new;
        return;
    }
    while(last->next != NULL) {
        last = last->next;
    }

    last->next = new;
    return;

}


void printList(struct node* node){

    while(node != NULL){
        printf("%d -> ", node->val);
        node = node->next;
    } printf(" NULL\n");
}

int main(){
    struct node* root = NULL;

    insert_end(&root, 6);
    insert_front(&root, 7);
    insert_front(&root, 1);
    insert_end(&root, 4);
    insert_after(root->next, 8);


    printf("Created List is: ");
    printList(root);

    return 0;
}