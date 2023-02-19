#include <stdio.h>
#include <math.h>
#include <stddef.h>
#include <stdbool.h>

typedef struct Stack{
    unsigned int capacity;
    int* items;
    int top;
} Stack;

int count = 0;

void create(Stack *s){
    (Stack *)malloc(sizeof(Stack));
    s->top = -1;
}

void del(Stack *s){
    (Stack *)free(sizeof(Stack));
}

bool is_empty(Stack *s){
    if(s->top == -1){
        return true;
    } else {return false;}
}

bool is_full(Stack *s){
if(s->top == s->items-1){
    return true; } 
    else { return false; }
}

int get_capacity(Stack s){
    printf("The capacity of the stack is: %i", s.capacity);
    return 0;
}

int num_items(){

}

void push(Stack *s, int new){
    if(is_full(s)){
        printf("Stack is full");
    } else {
        s->top++;
        s->items[s->top] = new;
    }
    count++;
}

void pop(){
    if(is_empty(s)){
        printf("\n Stack is empty! \n");
    } else {
        printf("Popped item: %d", s->items[s->top]);
        s->top--:
    }
    count--;
    
}

void peek(){

}

void print(Stack *s){
    printf("Stack: ");
    for(int i = 0; i < count; i++){
        printf("%d ", s->items[i]);
    }
    printf("\n");
}

bool is_equal(){

}

void reverse(){

}


int main(){

}