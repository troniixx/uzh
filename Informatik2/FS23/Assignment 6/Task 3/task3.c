#include <stdio.h>
#include <stdlib.h>
#define N 10

struct node{
    int key;
    struct node* next;
};


struct node* convertArraytoLinkedList(int *arr, int n); void print(struct node* curr); struct node* reverseLinkedList(struct node* head);

int main(){
    int *arr;
    arr = malloc(N*sizeof(int));

    for(int i = 0; i < N; i++){
        *(arr + i) = rand();
    }

    struct node *head = convertArraytoLinkedList(arr, N);

    printf("\nThe original");
    print(head);

    struct node* newHead = reverseLinkedList(head);

    printf("\nThe reversed");
    print(newHead);

    return 0;
}

struct node *convertArraytoLinkedList(int *arr, int n){
    struct node* root = NULL;

    for(int i = 0; i < n; i++){

    }
    
    return nullptr;
}

void print(struct node *curr){
    while(curr != NULL){
        printf("%d -> ", curr->key);
        curr = curr->next;
    }
}


struct node *reverseLinkedList(node *head){

    return nullptr;
}
