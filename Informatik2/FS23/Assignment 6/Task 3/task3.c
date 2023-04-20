#include <stdio.h>
#include <stdlib.h>
#define N 10

struct node{
    int key;
    struct node* next;
};


struct node* convertArraytoLinkedList(int *arr, int n); void print(struct node* curr); struct node* reverseLinkedList(struct node* head); struct node *reverse(struct node* prev, struct node* curr);

int main(){
    int *arr;
    arr = malloc(N*sizeof(int));

    for(int i = 0; i < N; i++){
        *(arr + i) = rand();
    }

    struct node *head = convertArraytoLinkedList(arr, N);

    printf("\nThe original: ");
    print(head);

    struct node* newHead = reverseLinkedList(head);

    printf("\nThe reversed: ");
    print(newHead);

    return 0;
}

struct node *convertArraytoLinkedList(int *arr, int n){
    struct node *newNode;
    newNode = malloc(sizeof(struct node));
    newNode->key = *(arr);

    struct node* curr = newNode;
    for(int i = 0; i < N; i++){
        curr->next = malloc(sizeof(struct node));
        curr = curr->next;
        curr->key = arr[i];
        curr->next = NULL;
    }
    
    return newNode;
}

void print(struct node *curr){
    while(curr != NULL){
        printf("%d ", curr->key);
        curr = curr->next;
    }
}


struct node *reverseLinkedList(struct node *head){
    struct node** h = malloc(sizeof(struct node*));
    *h = malloc(sizeof(struct node*));
    reverse(*h, head);

    return (*h)->next;
}

struct node *reverse(struct node* prev, struct node* curr){
    if(curr->next == NULL){
        prev->next = curr;
        return curr;
    }

    struct node* temp = reverse(prev, curr->next);
    temp->next = curr;
    curr->next = NULL;

    return curr;
}
